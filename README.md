<h1 align="center">Welcome to PhoneMate</h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

# Phonemate

Phonemate is a project that recommends phones to users based on the options they select. It consists of a Python Flask API for the backend, a React frontend, and uses MySQL as the database. The backend is deployed on Amazon EC2 with a load balancer, while the frontend is deployed on AWS Amplify. The project is open source and released under the MIT License

## Tech Stack

**Frontend:** React, scss

**Backend:** Flask, SQLAlchemy

**Database:** MySql, RDS

**Server:** AWS EC2, AWS Amplify, AWS LoadBalancer

![Tech Stack Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvpy4_gkGV4gTvrsL2AMoJ2pH6mqxOzhTLpw&usqp=CAU) ![Tech Stack Logo](https://www.datocms-assets.com/45470/1631110818-logo-react-js.png)

![Tech Stack Logo](https://res.cloudinary.com/practicaldev/image/fetch/s--QsmIiz9y--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/lnm6ybztq944ikym1s8f.JPG)


## Features

- Recommends phones based on user-selected options.
- Provides a user-friendly interface for easy interaction.
- Backend API built with Python Flask for efficient data processing.
- Frontend developed using React for a responsive and dynamic user experience.
- Utilizes MySQL database for storing phone data and user preferences.
- Scalable deployment on Amazon EC2 with load balancing for high availability.
- Easy deployment of frontend on AWS Amplify for seamless integration.
- Data scraped from gadgets360.com to populate the phone database

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`FLASK_APP`

`SQLALCHEMY_DATABASE_URI`


## Getting Started

Clone the project

```bash
  git clone https://github.com/leroydsilva/PhoneMate.git
```

Go to the project directory

```bash
  cd PhoneMate
```

Create a virtual environment for the project:

```bash
  python3 -m venv venv
```
Activate the virtual environment:

On macOS and Linux:
```bash
  source venv/bin/activate 
```
On Windows:
```bash
venv\Scripts\activate
```
Install the project dependencies:
```bash
pip install -r requirements.txt
```

Set up the frontend submodule:
```bash
git submodule init
git submodule update
cd frontend
```
Install the required dependencies:
```bash
npm start
```
Start the development server:

Start the backend server:
```bash
python run.py
```
Start the frontend development server:
```bash
npm start
```
Access the Phonemate application at http://localhost:3000 in your browser.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [gadgets360](https://www.gadgets360.com/)
 


## Feedback

If you have any feedback, please reach out to me at dsilva.leroy10@gmail.com
## Author

👤 **Leroy Dsilva**

* Github: [@leroydsilva](https://github.com/leroydsilva)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/leroydsilva\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/leroydsilva\/)

