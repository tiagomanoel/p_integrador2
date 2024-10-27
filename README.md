Aqui está o conteúdo completo do `README.md` com as instruções integradas, permitindo que o usuário defina o local do projeto ao configurar a execução automática usando `systemd`:

```markdown
# 📚 Projeto Integrador - UNIVESP (PJI)

---

## 📖 Overview

The **Projeto Integrador - UNIVESP** is a comprehensive web application designed to provide real-time data on currency exchange rates in Brazilian Real (BRL). This project was developed as part of the UNIVESP curriculum, emphasizing the practical application of programming and software development concepts.

### 🌟 Objectives

The primary objectives of the PJI include:

- **Real-time Currency Exchange Data**: Users can access updated exchange rates, allowing for informed financial decisions.
- **Historical Data Analysis**: The application provides historical data on currency values, enabling users to analyze trends over time.
- **User-Friendly Interface**: Designed with user experience in mind, the application boasts an intuitive layout that simplifies navigation and information retrieval.
- **Scalability**: Built on robust technologies that allow for future enhancements and increased user demand.

---

## 💻 Application Description

### Key Features

1. **Live Updates**: The application fetches real-time currency exchange rates from an external API, ensuring that users have access to the latest information.
  
2. **Historical Data Visualization**: Users can view a history of currency values, facilitating analysis of exchange rate trends over specified periods.

3. **Intuitive UI/UX**: The layout is designed to be straightforward and responsive, making it accessible on various devices.

4. **API Integration**: The application exposes a RESTful API for developers to interact with, offering endpoints to retrieve currency data programmatically.

5. **Multi-Currency Support**: Although focused on BRL, the application can easily be expanded to include other currencies.

### User Journey

- **Landing Page**: Users are greeted with a clean and informative landing page that summarizes the application's functionalities.
- **Currency Selection**: Users can select the currency they wish to monitor or analyze.
- **Data Retrieval**: Upon selection, the application fetches relevant data, displaying it in a user-friendly format, including charts and tables.

### Target Audience

- **Individuals**: People seeking to keep track of currency rates for personal or business purposes.
- **Developers**: Software developers looking for financial data to integrate into their applications.
- **Students**: Learners in finance or economics who wish to analyze currency trends.

---

## 🛠️ Technologies Used

The PJI leverages a modern tech stack to ensure reliability, performance, and maintainability. Below are the primary technologies used in the development of the application:

- **Django**: High-level Python web framework.
- **Django REST Framework (DRF)**: Toolkit for building Web APIs.
- **PostgreSQL**: Open-source relational database.
- **Docker**: Containerization for consistent environments.
- **Bootstrap**: Front-end framework for responsive design.
- **XML and JSON**: Formats for data interchange.

---

## 📊 Data Sources

The application relies on external APIs like **AwesomeAPI** to fetch real-time currency data, ensuring accuracy for users.

---

## 🛠️ Development Setup

### Prerequisites

- **Docker**
- **Docker Compose**
- **Python 3.12+** (if not using Docker)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tiagomanoel/p_integrador2.git
   cd p_integrador2
   ```

2. **Create a `.env` File**

   ```bash
   POSTGRES_HOST=psql
   POSTGRES_PORT=5432
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   ```

3. **Edit the `request_api.py` File**

   - Configure API settings in `scripts/request/request_api.py` as needed.

4. **Build the Docker Containers**

   ```bash
   docker-compose up --build
   ```

5. **Run the Django Application**

   ```bash
   docker-compose run djangoapp python manage.py runserver
   ```

6. **Access the Application**

   Navigate to `http://localhost:8000`.

---

## 🛠️ Configuring Automatic Execution with `systemd`

### Step 1: Create a Startup Script

1. Navigate to the project directory (replace with your own path):

   ```bash
   cd /path/to/your/project/
   ```

2. Create the `start_project.sh` script:

   ```bash
   #!/bin/bash
   cd /path/to/your/project/
   docker-compose up -d
   docker-compose run djangoapp python manage.py runserver
   ```

3. Make the script executable:

   ```bash
   sudo chmod +x /path/to/your/project/start_project.sh
   ```

### Step 2: Create a `systemd` Service

1. Create a service file:

   ```bash
   sudo nano /etc/systemd/system/your_project.service
   ```

2. Add the following content (adjust paths accordingly):

   ```ini
   [Unit]
   Description=Start Django and Docker Project
   After=docker.service
   Requires=docker.service

   [Service]
   Type=simple
   ExecStart=/path/to/your/project/start_project.sh
   WorkingDirectory=/path/to/your/project/
   Restart=always
   User=root

   [Install]
   WantedBy=multi-user.target
   ```

3. Save and exit the editor.

### Step 3: Enable and Start the Service

1. Reload the `systemd` configuration:

   ```bash
   sudo systemctl daemon-reload
   ```

2. Enable the service to start at boot:

   ```bash
   sudo systemctl enable your_project.service
   ```

3. Start the service manually:

   ```bash
   sudo systemctl start your_project.service
   ```

### Step 4: Check Service Status

Check if the service is running:

```bash
sudo systemctl status your_project.service
```

If everything is set up correctly, the service should show as "active (running)."

### Step 5: Reboot and Test

After setting up the service, you can reboot the server to test:

```bash
sudo reboot
```

---

## 🧑‍💻 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make changes and commit (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## 📞 Contact

- **Email**: tiago.g.manoel@proton.me
- **GitHub**: [Tiago Giglia Manoel](https://github.com/tiagomanoel/p_integrador2)

---

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.
```

---

