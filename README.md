Sure! Here’s the entire `README.md` content in a single code block:

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

### 1. **Django**

- A high-level Python web framework that promotes rapid development and clean, pragmatic design.
- Benefits include:
  - **Robust ORM**: Efficient database interactions without the need for complex SQL queries.
  - **Admin Interface**: Automatically generated admin panels for easy content management.
  - **Security**: Built-in protections against common web vulnerabilities such as SQL injection and cross-site scripting (XSS).

### 2. **Django REST Framework (DRF)**

- A powerful toolkit for building Web APIs in Django.
- Key Features:
  - **Serialization**: Converting complex data types such as querysets into JSON or XML for easy consumption.
  - **Authentication**: Support for various authentication schemes, including token-based and session-based authentication.
  - **Browsable API**: A user-friendly interface for testing API endpoints.

### 3. **PostgreSQL**

- An advanced, open-source relational database management system.
- Advantages:
  - **Scalability**: Can handle large datasets efficiently.
  - **ACID Compliance**: Ensures reliable transactions.
  - **Extensibility**: Supports custom data types and functions.

### 4. **Docker**

- Containerization technology that allows developers to package applications and their dependencies into a single container.
- Benefits:
  - **Consistency**: Eliminates issues related to environment differences across development, testing, and production.
  - **Isolation**: Each container runs independently, ensuring that applications do not interfere with one another.

### 5. **Bootstrap**

- A front-end framework for developing responsive and mobile-first websites.
- Features:
  - **Predefined Components**: Ready-to-use components such as buttons, modals, and navigation bars.
  - **Grid System**: Flexible grid layout for responsive designs.

### 6. **XML and JSON**

- Formats used for data interchange.
- The application uses XML to parse currency data from external sources and JSON to communicate with the frontend.

---

## 📊 Data Sources

The application relies on external APIs to fetch real-time currency data. Specifically, the **AwesomeAPI** is utilized to provide reliable and updated exchange rates, ensuring accuracy for the end-users.

---

## 🛠️ Development Setup

### Prerequisites

To run the application locally, ensure you have the following installed:

- **Docker**: For containerization of the application.
- **Docker Compose**: For managing multi-container Docker applications.
- **Python 3.12+** (if not using Docker).

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tiagomanoel/p_integrador2.git
   cd p_integrador2
   ```

2. **Create a `.env` File**

   Define your environment variables in a `.env` file at the root of the project:

   ```
   POSTGRES_HOST=psql
   POSTGRES_PORT=5432
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   ```

3. **Edit the `request_api.py` File**

   - Open `scripts/request/request_api.py` and configure any necessary settings, such as API keys or endpoints, as needed for your specific use case.

4. **Build the Docker Containers**

   Use Docker Compose to build the application containers:

   ```bash
   docker-compose up --build
   ```

5. **Run the Django Application**

   After building the containers, run the Django application with the following command:

   ```bash
   docker-compose run djangoapp python manage.py runserver
   ```

6. **Access the Application**

   Navigate to `http://localhost:8000` in your web browser to access the application.

---

## 🧑‍💻 Contributing

Contributions are welcome! If you'd like to enhance this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## 📞 Contact

For inquiries or further information, feel free to reach out:

- **Email**: tiago.g.manoel@proton.me
- **GitHub**: [Tiago Giglia Manoel](https://github.com/tiagomanoel/p_integrador2)

---

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

