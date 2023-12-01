import os
import shutil
from pathlib import Path
import tempfile
import os
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from prophecy_pybridge.controller.file_controller import FileController
import subprocess


class HdfsController(object):

    @staticmethod
    def _run_cmd(bash_command: list[str]) -> object:
        result = subprocess.run(bash_command, shell=True, text=True, capture_output=True)
        return result

    @staticmethod
    def upload_file(file: UploadFile = File(...), destination_dir: str = None):
        """
        Uploads a file to the specified destination directory in HDFS.

        :param file: The file to be uploaded.
        :param destination_dir: The destination directory in HDFS.
        :return: A JSON response indicating the status of the upload process.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            print(f"Temporary directory created: {temp_dir}")

            # upload file to tmp directory
            file_upload_result = FileController.upload_file(file, temp_dir)
            if file_upload_result.status_code != 200:
                return file_upload_result

            # now, we will move run hdfs command
            temp_file_path = os.path.join(temp_dir, file.filename)
            result = HdfsController._run_cmd(f"hdfs dfs -copyFromLocal {temp_file_path} {destination_dir}")
            if result.returncode == 0:
                print(f"Command executed successfully: {result}")

                return JSONResponse(
                    status_code=200, content={
                        "message": f"file {file.filename} copied to hdfs location {destination_dir} successfully!",
                        "details": result.stdout
                    }
                )
            else:
                print(f"Command failed with return code: \n{result}\n")
                return JSONResponse(
                    status_code=500, content={
                        "message": f"Error copying {file.filename} to hdfs location {destination_dir}",
                        "details:": result.stderr
                    }
                )

    @staticmethod
    def delete_file(file_path: str):
        result = HdfsController._run_cmd(f"hdfs dfs -rm {file_path}")

        if result.returncode == 0:
            print(f"file {file_path} has been removed successfully\n {result}\n")
            return JSONResponse(
                status_code=200, content={
                    "message": f"file {file_path} has been removed successfully: {result}",
                    "details": result.stdout
                }
            )
        else:
            print(f"Error deleting hdfs file \n{result}\n")
            return JSONResponse(
                status_code=500, content={
                    "message": f"Error deleting hdfs file {file_path}",
                    "details:": result.stderr
                }
            )

    @staticmethod
    def delete_directory(directory_path: str):
        try:
            shutil.rmtree(directory_path)
            return JSONResponse(
                content={
                    "message": f"File {directory_path} deleted recursively successfully."
                }
            )
        except OSError as e:
            print(f"Error deleting directory {directory_path}: {e}")
            return JSONResponse(
                status_code=500,
                content={
                    "error": f"Error deleting directory {directory_path}",
                    "details": f" {e}",
                },
            )
