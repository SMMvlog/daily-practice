from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 10, txt="Mehboob Shaikh", ln=True, align="C")
pdf.cell(200, 10, txt="Python Backend Developer", ln=True, align="C")
pdf.cell(200, 10, txt="", ln=True)

# Contact Details
pdf.multi_cell(0, 10, txt="""Location: Dargah Road, Moin Apartment, Amrut Nagar, Mumbra, Thane 400612
Mobile: +91 8828319602
Email: mehboob61923@gmail.com
GitHub: https://github.com/SMMvlog""")
pdf.cell(200, 10, txt="", ln=True)

# Professional Summary
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="PROFESSIONAL SUMMARY", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""A highly skilled and reliable Python Backend Developer with 4.7+ years of experience in developing and deploying APIs and backend solutions for various domains including finance, e-commerce, and auctions. Adept at utilizing frameworks such as Django, Flask, and Falcon, with expertise in cloud services and database management. Known for quick learning, being a team player, and a strong sense of responsibility in production environments.""")
pdf.cell(200, 10, txt="", ln=True)

# Experience Section
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="EXPERIENCE", ln=True)
pdf.set_font("Arial", size=12)

# Experience 1
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="Python Flask and Falcon API Developer", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Aditya Birla Finance Limited, Thane
March 2024 – Present
Vendor: MITS Global Consulting
- Developing and maintaining Flask APIs for finance-related products.
- Working on backend development, coding, and production activities.
- Handling cloud services such as AWS CloudWatch, S3, and DynamoDB.
- Contributed to the development of the One App platform (One App URL: https://oneapp.abfldirect.com/aucc/index).""")
pdf.cell(200, 10, txt="", ln=True)

# Experience 2
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="Python Django API Developer", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Vishleshan Pvt Ltd, Chandivli
June 2021 – January 2024
- Developed and maintained APIs using Django Rest Framework.
- Successfully worked on 5 projects for clients like Tata Motors and Tata Finance.
- Deployed and managed projects on AWS, using S3 for storage.
- Developed key APIs, such as vehicle dropdown and part search, using Pandas for data manipulation.""")

# Experience 3
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="Python Django Developer", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""FutureTech Software, Kharghar
October 2019 – May 2021
- Started as an intern and transitioned into a full-time Python Django Backend Developer.
- Worked extensively on Django templates and Jinja for various backend solutions.""")

# Experience 4
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="Freelance Front-End Developer", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""June 2017 – May 2019
- Designed and developed responsive front-end templates using HTML, CSS, and Bootstrap for various clients.""")

# Education Section
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="EDUCATION", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Bachelor of Science in Computer Science
Maharashtra College, Byculla
October 2016 | Mumbai University""")

# Projects Section
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="PROJECTS", ln=True)
pdf.set_font("Arial", size=12)

# Project 1
pdf.multi_cell(0, 10, txt="""Tata Motors Rewire | Sell Old Vehicles
Client: Tata Motors
- Developed APIs for a platform where users can sell vehicles based on their condition.
- Role: Involved in requirement gathering, API development, and deployment.""")

# Project 2
pdf.multi_cell(0, 10, txt="""Tata Ecom Edukaan | Sell Vehicle Parts
Client: Tata Motors
- Developed APIs for an e-commerce platform that sells genuine Tata Motors vehicle parts.
- Role: Created and deployed APIs on both local and production servers.""")

# Project 3
pdf.multi_cell(0, 10, txt="""Wheels Deals | Auction Platform
Client: Tata Motors Finance Ltd
- Built an auction-based platform for Tata Finance to sell repossessed vehicles.
- Role: Developed both admin and customer portals, created APIs, and contributed to requirement gathering.""")

# Project 4
pdf.multi_cell(0, 10, txt="""One App | E-Finance Platform
Client: Aditya Birla
- Developed APIs for managing customer records and implementing login functionalities for a loan-based application.
- Role: Involved in requirement gathering, API development, and deployment.""")

# Skills Section
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, txt="TECHNICAL SKILLS", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""- Programming Languages: Python
- Frameworks: Django, Flask, Falcon
- APIs: Django Rest Framework, Flask APIs
- Databases: PostgreSQL, MySQL, DynamoDB
- Tools: GitHub, GitLab, Postman, S3 Browser
- Cloud Services: AWS (S3, EC2, CloudWatch)
- Data Analysis: Pandas
- Front-end Basics: HTML, CSS, Bootstrap""")

# Languages Section
pdf.set_font("Arial",size=12)

pdf.output(r"C:\Users\mehbo\Desktop\for test\.vscode\resume.pdf")