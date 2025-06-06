pip install Flask tabulate
python app.py

---

## Deploying to PythonAnywhere (Free Tier)

This application can be deployed to PythonAnywhere, which offers a free tier suitable for small Flask applications.

### Steps:

1.  **Sign up for PythonAnywhere:**
    *   Go to [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/) and create a free "Beginner" account.

2.  **Upload Your Project:**
    *   **Option A (Recommended): Using Git**
        *   Push your project (including `requirements.txt`, `wsgi.py`, and the `IPL-3.0` directory) to a GitHub (or similar) repository.
        *   On PythonAnywhere, open a "Bash Console" from your Dashboard.
        *   Clone your repository: `git clone <your-repository-url>`
        *   This will create a directory with your project files. Note the path to this directory (e.g., `/home/YourUserName/your-project-name/`).
    *   **Option B: Manual Upload**
        *   From the PythonAnywhere "Files" tab, you can upload your files individually or as a zip archive (and then unzip it in a Bash console). Make sure the `IPL-3.0` directory, `requirements.txt`, and `wsgi.py` are uploaded into a project directory (e.g., `/home/YourUserName/my-ipl-app/`).

3.  **Create a Web App:**
    *   Go to the "Web" tab on PythonAnywhere.
    *   Click "Add a new web app".
    *   Confirm your domain name (e.g., `yourusername.pythonanywhere.com`).
    *   Select "Flask" as the Python web framework.
    *   Choose the Python version that matches your project (e.g., Python 3.10). PythonAnywhere will create a default Flask app structure and a WSGI configuration file. We will modify this WSGI file.

4.  **Configure the WSGI File:**
    *   In the "Code" section of your Web app tab on PythonAnywhere, find the "WSGI configuration file" link. Click it to edit the file (it will be something like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
    *   **Replace the entire content** of this PythonAnywhere WSGI file with the content of the `wsgi.py` file located in the root of your uploaded project.
        *   You'll need to adjust the `project_home` variable in the WSGI file content if your project is not in the root directory of where PythonAnywhere expects it or if your main application directory isn't `IPL-3.0`.
        *   Specifically, ensure the line `project_home = os.path.abspath(os.path.join(os.path.dirname(__file__), 'IPL-3.0'))` in your `wsgi.py` correctly points to the `IPL-3.0` directory relative to where PythonAnywhere places the WSGI file, OR provide an absolute path.
        *   A common setup on PythonAnywhere, if you cloned your repo named `my-ipl-repo` into `/home/YourUserName/`, would be to set `project_home` in the PythonAnywhere WSGI file like this:
            ```python
            # project_home = '/home/YourUserName/my-ipl-repo/IPL-3.0' # Path to the IPL-3.0 folder
            # For the provided wsgi.py, it assumes IPL-3.0 is a subdirectory relative to wsgi.py's parent.
            # If your wsgi.py is at /home/YourUserName/my-ipl-repo/wsgi.py, then the line:
            # project_home = os.path.abspath(os.path.join(os.path.dirname(__file__), 'IPL-3.0'))
            # in wsgi.py might resolve correctly if PythonAnywhere's actual wsgi file is also in /home/YourUserName/my-ipl-repo/
            # However, PythonAnywhere's WSGI file is typically at /var/www/.
            # So, you MUST update the path in the PythonAnywhere WSGI editor:
            #
            # Example content for /var/www/yourusername_pythonanywhere_com_wsgi.py:
            # +++++++++++++++++++++++++++++++++++++++++++++++++++
            import sys
            import os

            # Assuming your project is cloned/uploaded to /home/YourUserName/your-project-directory-name/
            # And your Flask app 'app.py' is inside /home/YourUserName/your-project-directory-name/IPL-3.0/
            path_to_app_dir = '/home/YourUserName/your-project-directory-name/IPL-3.0'
            if path_to_app_dir not in sys.path:
                sys.path.insert(0, path_to_app_dir)

            # Change to the app directory
            os.chdir(path_to_app_dir)

            from app import app as application
            # +++++++++++++++++++++++++++++++++++++++++++++++++++
            ```
        *   **Important**: Adjust `/home/YourUserName/your-project-directory-name/` to your actual PythonAnywhere username and the directory where you cloned/uploaded your project.

5.  **Set up a Virtual Environment and Install Dependencies:**
    *   Still in the "Web" tab on PythonAnywhere, scroll down to the "Virtualenv" section.
    *   Specify a path for your virtual environment, for example: `/home/YourUserName/.virtualenvs/ipl-app-venv`.
    *   Click "Create" or, if it's already created, click the link to open a bash console in that virtualenv.
    *   If you just created it, PythonAnywhere might pre-fill a command like `mkvirtualenv --python=/usr/bin/python3.10 myenv`. Run it if prompted.
    *   Once the virtualenv is active (you'll see its name in the console prompt), navigate to your project directory that contains `requirements.txt` (e.g., `cd /home/YourUserName/your-project-name/IPL-3.0/`).
    *   Install the dependencies: `pip install -r requirements.txt`

6.  **Reload Your Web App:**
    *   Go back to the "Web" tab on PythonAnywhere.
    *   Click the big green "Reload <yourusername>.pythonanywhere.com" button.

7.  **Access Your Website:**
    *   Your website should now be live at `http://<yourusername>.pythonanywhere.com`.

### Troubleshooting:

*   **Check Error Logs:** If something goes wrong, the "Error log" and "Server log" links on the PythonAnywhere "Web" tab are very helpful.
*   **File Paths:** Double-check all file paths in your WSGI configuration and within your application for correctness in the PythonAnywhere environment.
*   **Working Directory:** Ensure your application's working directory is correctly set in the WSGI file if it relies on relative paths for accessing data files (like `teams/teams.json` or `tmp_match_logs/`). The `os.chdir(path_to_app_dir)` in the example WSGI content above helps with this. The application creates `scores_dir_path` and `TMP_LOG_DIR` relative to its CWD.
*   **Static Files:** For CSS, JavaScript, and images, you might need to configure static file mappings under the "Static files" section of the "Web" tab on PythonAnywhere.
    *   URL: `/static/`
    *   Directory: `/home/YourUserName/your-project-name/IPL-3.0/static/` (if you create a static folder there). Your current app does not seem to use a `/static` folder for CSS/JS as it's embedded or linked from `templates`. Flask serves `static` by default if it's next to `templates`.

---