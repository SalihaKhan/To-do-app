"""
Package script for the Todo CLI skill.
Creates a distributable package of the skill following the specified requirements.
"""

import os
import shutil
import zipfile
from pathlib import Path


def create_skill_package():
    """
    Create a distributable package of the Todo CLI skill.
    """
    print("Creating Todo CLI skill package...")
    
    # Define source and destination paths
    source_dir = Path("todo_cli")
    package_name = "todo_cli_skill"
    zip_filename = f"{package_name}.zip"
    
    # Create a temporary directory for packaging
    temp_dir = Path("temp_package")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    
    # Copy the entire todo_cli directory to the temp directory
    dest_dir = temp_dir / package_name
    shutil.copytree(source_dir, dest_dir)
    
    # Add the SKILL.md file to the package
    shutil.copy("SKILL.md", dest_dir / "SKILL.md")
    
    # Create the package zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dest_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(temp_dir)
                zipf.write(file_path, arc_path)
    
    # Clean up temporary directory
    shutil.rmtree(temp_dir)
    
    print(f"SUCCESS: Skill package created: {zip_filename}")
    print(f"SUCCESS: Package contains the complete Todo CLI skill")
    print(f"SUCCESS: Ready for distribution and reuse")


def verify_package_contents():
    """
    Verify the contents of the created package.
    """
    print("\nVerifying package contents...")
    
    package_name = "todo_cli_skill"
    zip_filename = f"{package_name}.zip"
    
    # Check if the zip file exists
    if not os.path.exists(zip_filename):
        print(f"✗ Package file {zip_filename} not found")
        return False
    
    # List contents of the zip file
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        contents = zipf.namelist()
        
        # Verify required components are present
        required_files = [
            "todo/__init__.py",
            "todo/task.py",
            "todo/task_manager.py",
            "tests/__init__.py",
            "tests/test_todo.py",
            "cli.py",
            "__init__.py",
            "SKILL.md"
        ]
        
        for file in required_files:
            expected_path = f"{package_name}/{file}"
            if expected_path not in contents:
                print(f"ERROR: Required file missing: {expected_path}")
                return False

    print("SUCCESS: All required files are present in the package")
    print("SUCCESS: Package verification completed successfully")
    return True


if __name__ == "__main__":
    create_skill_package()
    verify_package_contents()
    print("\nTodo CLI skill packaging completed successfully!")