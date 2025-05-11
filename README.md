# CyberSecurity_Lab4

This project is a simple Flask-based web application intentionally designed with common security vulnerabilities for educational and testing purposes. It contains two major flaws: **SQL Injection** and **Cross-Site Scripting (XSS)**, which are commonly discussed in web application security courses. The app is fully Dockerized for easy setup and consistent deployment.

---

## Key features

- **Search Users**: A form that queries users based on input — **vulnerable to SQL Injection**
- **Comment System**: Users can submit comments that are displayed without sanitization — **vulnerable to XSS**
- Docker support for sandboxed testing

---

## Setup Instructions

### Prerequisites
- Docker installed on your machine

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/minimonomana/CyberSecurity_Lab4.git
   cd vuln
    ```
2. **Build the Docker image**:
   ```bash
   docker build -t vuln .
   ```

3. **Run the Docker container**:
   ```bash
    docker run -p 5000:5000 vuln
    ```
4. **Access the application**:

    Open your web browser and navigate to `http://localhost:5000`.

5. **Test the vulnerabilities**:
    - For SQL Injection, go to the **User Search** page and input:
      ```sql
      ' OR '1'='1
      ```
    - For XSS, go to the **Comment Box** and input:
      ```html
      <script>alert('XSS')</script>
      ```