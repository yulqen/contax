# Contax - A Simple Contact Manager

Contax is a simple contact management application built with Django that helps users to store and manage their contacts. The application features a user-friendly interface, allowing users to create, update, delete contacts easily. 

## Features

- **Contact Management**: Create, read, update, and delete contacts.
- **Favourite Contacts**: Mark contacts (by clicking the star icon) as favourites for quick visual access. (Filtering or sorting by favourites could be an additional feature).
- **Responsive Design**: Accessible on mobile and desktop devices.

## Getting Started

### Prerequisites

To run this application, ensure you have Python 3.11 or above installed on your Ubuntu or Debian machine (or similar flavour of Linux):

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

   Use `pipx` to install `uv`:

   ```bash
   pipx install uv
   ```

3. **Clone the Repository**

   Clone the Contax repository from Github:

   ```bash
   git clone https://github.com/yulqen/contax
   cd contax
   ```

4. **Run the migrations**

   ```bash
   uv run manage.py migrate
   ```

5. **Run the tests**

   To run the tests for the API and the browser-based views:

   ```bash
   uv run pytest -q
   ```

6. **Start the Server**

   To run the development server, execute the following command:

   ```bash
   uv run manage.py runserver
   ```

### Accessing the Application

You can access the application by opening your web browser and navigating to:

```
http://localhost:8000
```

Click the "New Contact" button on the top right of the page to add a new contact to the system.

Hint: click on the star icon to add a contact as favourite after it has been added. It uses **htmx**!

You can interact with the rudimentary API via the browser:

```
http://localhost:8000/api/contacts
```

or use CLI tools like `curl` to access the same URL and obtain `json` output for further processing.

### Access the admin application

To access Django's admin site, you need to create an admin user first:

```bash
uv run manage.py createsuperuser
```

Then log in using those credentials:

```
http://localhost:8000/admin
```

## Deploying on Google Cloud Platform

To deploy this Django application on Google Cloud Platform (GCP), specifically Google App Engine:

1. **Prerequisite Installations**: Ensure you have the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed on your local machine.

2. **Create a Google Cloud Project**: If you do not have one, [create a project in the GCP Console](https://console.cloud.google.com/projectselector2/home/dashboard).

3. **Google Cloud Storage Setup**: Set up Google Cloud Storage to host your media files. Ensure to configure permissions appropriately so that your Django app can access it.

4. **App Engine Setup**: Use the Google Cloud Console to [set up App Engine](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com,secretmanager.googleapis.com,cloudbuild.googleapis.com) for your project, and [initialise it](https://cloud.google.com/sdk/docs/initializing).

5. **Ensure latest documentation on finalising the configuration is followed**: Follow steps in [Google App Engine for Django](https://cloud.google.com/python/django/appengine).

6. **Access the Deployed Application**: Once the deployment is successful, you can access your application via the URL provided in the deployment output.

## License

This project is licensed under the AGPL License. See the [LICENSE](LICENSE) file for details.

---

If you face issues, feel free to raise an issue in the project repository. Enjoy managing your contacts with Contax!
