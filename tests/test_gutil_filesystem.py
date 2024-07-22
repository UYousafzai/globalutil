import unittest
import os
import sys
import shutil
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from globalutil.filesystem import (
    Inspect, Sort, FileSearch, FileOrganizer, FileAnalyzer,
    DirectoryManager, FileBackup, FileArchive, FileIntegrity,
    RecentFiles, FileRename
)

class TestGUtil(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Create sample files and directories
        os.makedirs(os.path.join(self.test_dir, "subdir"))
        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("This is file 1")
        with open(os.path.join(self.test_dir, "file2.txt"), "w") as f:
            f.write("This is file 2")
        with open(os.path.join(self.test_dir, "subdir", "file3.txt"), "w") as f:
            f.write("This is file 3")

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)

    def test_inspect(self):
        tree = Inspect.get_directory_tree(self.test_dir)
        self.assertIn("file1.txt", tree)
        self.assertIn("file2.txt", tree)
        self.assertIn("subdir", tree)

    def test_sort(self):
        dest_dir = os.path.join(self.test_dir, "sorted")
        Sort.copy(self.test_dir, dest_dir, patterns=["*.txt"])
        self.assertTrue(os.path.exists(os.path.join(dest_dir, "file1.txt")))
        self.assertTrue(os.path.exists(os.path.join(dest_dir, "file2.txt")))
        self.assertFalse(os.path.exists(os.path.join(dest_dir, "subdir", "file3.txt")))

    def test_file_search(self):
        found_files = FileSearch.find_files(self.test_dir, {"name": "file*.txt", "content": "This is file"})
        self.assertEqual(len(found_files), 3)

    def test_file_organizer(self):
        org_dir = os.path.join(self.test_dir, "organized")
        FileOrganizer.categorize_files(self.test_dir, org_dir)
        self.assertTrue(os.path.exists(os.path.join(org_dir, "documents", "file1.txt")))

    def test_file_analyzer(self):
        large_files = FileAnalyzer.find_large_files(self.test_dir, 1)  # Files larger than 1 byte
        self.assertEqual(len(large_files), 3)

    def test_directory_manager(self):
        empty_dir = os.path.join(self.test_dir, "empty")
        os.mkdir(empty_dir)
        removed = DirectoryManager.clean_empty_dirs(self.test_dir)
        self.assertIn(empty_dir, removed)

    def test_file_backup(self):
        backup_dir = os.path.join(self.test_dir, "backup")
        FileBackup.create_backup(os.path.join(self.test_dir, "file1.txt"), backup_dir)
        self.assertEqual(len(os.listdir(backup_dir)), 1)

    def test_file_archive(self):
        archive_path = os.path.join(self.test_dir, "archive.zip")
        FileArchive.create_archive(self.test_dir, archive_path)
        self.assertTrue(os.path.exists(archive_path))

    def test_file_integrity(self):
        file_path = os.path.join(self.test_dir, "file1.txt")
        checksum = FileIntegrity.calculate_checksum(file_path)
        self.assertTrue(FileIntegrity.verify_checksum(file_path, checksum))

    def test_recent_files(self):
        recent = RecentFiles.find_recent_files(self.test_dir, 1)  # Files modified in the last day
        self.assertEqual(len(recent), 3)

    def test_file_rename(self):
        FileRename.batch_rename(self.test_dir, "file", "document")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "document1.txt")))

if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGUtil)
    
    # Create a test runner with increased verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Run the tests
    result = runner.run(suite)
    
    # Print a summary
    print(f"\nRan {result.testsRun} tests")
    print(f"Successes: {result.testsRun - len(result.errors) - len(result.failures)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    # Exit with a non-zero code if there were failures or errors
    sys.exit(len(result.failures) + len(result.errors))