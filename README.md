# Number Classification API  

This project was assigned as **Task 1 for DevOps Interns** in the **HNG Internship 12** program. The goal is to build an API that classifies a given number, returning its mathematical properties along with a fun fact fetched from the [Numbers API](http://numbersapi.com).  

## **Project Description**  
<!-- Provide a brief description of the project here -->  
### **Project Description: Number Classification API**

The **Number Classification API** is a DevOps task designed to create a RESTful API that takes a number as input and returns its interesting mathematical properties along with a fun fact. The API leverages the **Numbers API** to fetch fun facts and implements logic to classify numbers based on properties like prime, perfect, Armstrong, odd/even, and digit sum.


### **Key Features**
1. **Number Classification**:
   - Determines if a number is **prime**, **perfect**, or an **Armstrong number**.
   - Checks if the number is **odd** or **even**.
   - Calculates the **sum of its digits**.

2. **Fun Fact Integration**:
   - Fetches a fun fact about the number from the **Numbers API**.

3. **RESTful Endpoint**:
   - Provides a `GET` endpoint to classify numbers and return results in JSON format.

4. **Public Accessibility**:
   - Deployed to a publicly accessible endpoint with **CORS** enabled for cross-origin requests.


### **Requirements**
1. **Technology Stack**:
   - Use any programming language or framework (e.g., Python, Node.js, Java, Go, etc.).
   - Must handle **CORS** for public access.
   - Must return responses in **JSON format**.

2. **Deployment**:
   - The API must be deployed to a publicly accessible endpoint (e.g., Google Cloud Platform, AWS, Heroku).

3. **Version Control**:
   - Code must be hosted on **GitHub** in a **public repository**.
   - Include a **well-structured README.md** with setup, usage, and deployment instructions.

4. **API Specification**:
   - **Endpoint**: `GET /api/classify-number?number=<number>`
   - **Response Format (200 OK)**:
     ```json
     {
       "number": 371,
       "is_prime": false,
       "is_perfect": false,
       "properties": ["armstrong", "odd"],
       "digit_sum": 11,
       "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
     }
     ```
   - **Response Format (400 Bad Request)**:
     ```json
     {
       "number": "abc",
       "error": true
     }
     ```


### **Resources**
1. **Fun Fact API**: [Numbers API](http://numbersapi.com/#42)
2. **Mathematical Properties**:
   - [Parity (Mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))
   - [Prime Numbers](https://en.wikipedia.org/wiki/Prime_number)
   - [Perfect Numbers](https://en.wikipedia.org/wiki/Perfect_number)
   - [Armstrong Numbers](https://en.wikipedia.org/wiki/Narcissistic_number)

### **Acceptance Criteria**
1. **Functionality**:
   - Accepts `GET` requests with a `number` parameter.
   - Returns JSON in the specified format.
   - Handles all valid integers as input.

2. **Code Quality**:
   - Organized code structure.
   - Basic error handling and input validation.
   - Avoids hardcoded values.

3. **Documentation**:
   - Complete `README.md` with project description, setup instructions, and API usage.

4. **Deployment**:
   - Publicly accessible and stable API.
   - Fast response time (< 500ms).


### **Submission**
- Ensure the API is hosted and tested thoroughly before submission.
- Deadline: **Friday, Feb 7th - 11:59pm GMT +1**.

---  

## **Project Structure**  
This repository contains two separate implementations of the Number Classification API:  
- **Express.js + Node.js** 
- **Django REST Framework** 

Additionally, an **Nginx** configuration is included to manage deployments.  

---  

## **Deployed Endpoints**  
Both solutions have been deployed and are accessible via the following URLs:  

- **Express.js API Endpoint**:  
  `[Insert Express.js Deployment URL]`  

- **Django API Endpoint**:  
  `[Insert Django Deployment URL]`  

Each endpoint follows the same API structure, accepting a `GET` request with an integer number parameter and returning JSON responses.  

---  

## **Technologies Used**  
- **Backend**: Express.js (Node.js) & Django REST Framework (Python)  
- **External API**: [Numbers API](http://numbersapi.com)  
- **Containerization**: Docker  
- **Reverse Proxy**: Nginx  
- **Deployment**: Google Cloud Platform (Cloud Run)  
- **Version Control**: GitHub  

---  

## **Setup and Installation**  
Each solution has its own setup instructions inside its respective folder (`express` or `django`).  

To clone this repository:  

```bash
git clone https://github.com/your-username/number-classification-api.git  
cd number-classification-api  
