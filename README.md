# Contax - A Simple Contact Manager

Contax is a simple contact management application built with Django that helps users to store, manage, and share their contacts. The application features a user-friendly interface, allowing users to create, update, delete, and search for contacts easily. 

## Features

- **Contact Management**: Create, read, update, and delete contacts.
- **Search and Filter**: Easily search for contacts by name, email, or other fields, and filter favorites.
- **Favorite Contacts**: Mark contacts as favorites for quick access.
- **Responsive Design**: Accessible on mobile and desktop devices.

## Getting Started

### Prerequisites

To run this application, ensure you have the following installed on your **Ubuntu** machine:

- **Python 3.11 or above**
  
### Setup Instructions

1. **Install pipx**

   Ensure that you have `pipx` installed on your system. If `pipx` is not installed, you can install it by running:

   ```bash
   sudo apt install pipx
   ```

   After installation, restart your terminal or run:

   ```bash
   exec $SHELL
   ```

2. **Install `uv`**

   Use `pipx` to install the `uv` server:

   ```bash
   pipx install uv
   ```

3. **Clone the Repository**

   Clone the Contax repository from your source control:

   ```bash
   git clone https://github.com/yulqen/contax
   cd contax
   ```

4. **Run Migrations and Start the Server**

   To run the development server along with the necessary migrations, execute the following command:

   ```bash
   uv run manage.py migrate && uv run manage.py runserver
   ```

### Accessing the Application

You can access the application by opening your web browser and navigating to:

```
http://localhost:8000
```

Hint: click on the star icon to add a contact as favourite. It uses **htmx**!

## Deploying on Google Cloud Platform

To deploy this Django application on Google Cloud Platform (GCP):

1. **Prerequisite Installations**: Ensure you have the Google Cloud SDK installed on your local machine.

2. **Create a Google Cloud Project**: If you do not have one, create a project in the GCP Console.

3. **Google Cloud Storage Setup**: Set up Google Cloud Storage to host your media files. Ensure to configure permissions appropriately so that your Django app can access it.

4. **App Engine Setup**: Use the Google Cloud Console to set up App Engine for your project.

5. **Required Configuration**:
   - Create a `app.yaml` file in the root directory of your project with necessary configurations:
     ```yaml
     runtime: python311

     handlers:
     - url: /
       static_files: static/index.html
       upload: static/index.html

     - url: /(.+)
       static_files: \1
       upload: (.+)
     ```

6. **Deploy the Application**:
   Execute the following command from your terminal to deploy your application:

   ```bash
   gcloud app deploy
   ```

7. **Access the Deployed Application**: Once the deployment is successful, you can access your application via the URL provided in the deployment output.

## License

This project is licensed under the AGPL License. See the [LICENSE](LICENSE) file for details.

---

If you face issues, feel free to raise an issue in the project repository. Enjoy managing your contacts with Contax!
