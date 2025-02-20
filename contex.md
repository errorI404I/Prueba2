**Project Overview:**

You are tasked with developing a web application for a soccer training campus. The application consists of a backend, frontend, and a PostgreSQL database. The backend is developed using Python (FastAPI), and the frontend is developed using HTML5, CSS, and JavaScript. The application should be scalable, with a responsive design that works across both browsers and mobile devices. It should provide users with access to various campus activities, profiles, and other related functionalities.

**Backend Requirements:**

1. **Language & Framework:**
   - Backend is developed using Python and FastAPI.
   - REST API must follow OpenAPI standards.
   - Stateless session management using JWT tokens.

2. **Database:**
   - PostgreSQL is used for data storage.
   - The backend will be responsible for accessing and interacting with the database.
   - Implement ORM (SQLAlchemy) for managing interactions between the backend and the database.
   - Use Alembic for database migrations.

3. **API Functionalities:**
   - Implement CRUD (Create, Read, Update, Delete) operations for all application entities.
   - Business logic should be placed within the backend to ensure scalability.
   - Ensure the backend can handle high traffic and is easily scalable.
   - Send email notifications for important events (e.g., activity updates).

4. **Authentication:**
   - Implement JWT-based stateless authentication to protect user data.
   - Manage user roles and permissions within the backend.

5. **Error Handling:**
   - Implement proper error handling to return clear and appropriate messages for each type of error.

6. **Automated Testing:**
   - Include unit tests using pytest to ensure the API functionality is correctly implemented.

---

**Frontend Requirements:**

1. **Design & Responsiveness:**
   - The frontend must be fully responsive, supporting both mobile and desktop versions.
   - The design should be clean and simple, with no more than three clicks to reach the desired content.
   - Use HTML5, CSS, and JavaScript (no external state management libraries required).

2. **Sections and Navigation:**
   - The web application should have the following main sections:
     - Home: Displays the featured campus activities.
     - Calendar: Displays the upcoming 30 days of activities. Users can navigate through dates.
     - About Us: Provides information about the application.
     - Contact: Provides a form or contact details.
     - User Dashboard: The user's personal area for accessing their profile, preferences, and current activities.
   
3. **User Dashboard:**
   - After logging in, users are directed to their personalized dashboard.
   - The dashboard must support multiple views based on the user’s role (e.g., professor, participant).
   - The profile should include a picture, name, email, and description.

4. **API Consumption:**
   - The frontend will consume the REST API provided by the backend to display data dynamically (such as activities, profiles, etc.).
   
---

**Database Requirements:**

1. **Schema:**
   - Implement a schema that supports the following entities: 
     - User (with fields: name, email, picture, description, role)
     - Activity (with fields: professor, subject, place, schedule, description, price, available spots)
   
2. **Relationships:**
   - Define the relationships between entities (e.g., users can be professors, activities are associated with professors).

3. **Database Migration:**
   - Use Alembic for managing database schema changes.
   
---

**Server & Deployment Requirements:**

1. **Deployment:**
   - The backend should be deployable using Docker containers for easy scaling and management.
   - The application will be deployed on a cloud service (e.g., Vercel).

2. **Scalability:**
   - Ensure the backend can handle the expected traffic and can be easily scaled.

3. **Testing:**
   - Implement automated tests for both frontend (using Jest) and backend (using pytest).

---

**Development Process:**

The goal is to have a clear, structured development plan that will allow the AI to generate the code for each part of the application. Please iterate over each of these sections, ensuring clarity and detailed steps for generating the code.

---

Would you like to proceed with defining the individual sections in more detail, or is this sufficient for generating the first round of code for the project?