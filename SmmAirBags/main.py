from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy import create_engine,Column,String,Integer,Date,DateTime,func,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import date,datetime
app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:root@mysql_db:3306/proj1"

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,bind=engine,autoflush=False)
base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Department(base):
    __tablename__ = "emp_department"
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    update_at = Column(DateTime(timezone=True),server_default=func.now())

class Employee(base):
    __tablename__ = "my_employee"
    id = Column(Integer,primary_key=True,index=True)
    dept_id = Column(Integer,ForeignKey("emp_department.id"),nullable=True)
    name = Column(String(100),nullable=False)
    email_id = Column(String(120),nullable=False)
    salary = Column(Integer,nullable=False)
    joining_date = Column(Date,nullable=False)
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())

base.metadata.create_all(bind=engine)

class CreateDepartment(BaseModel):
    name :str

class GetDepartment(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True

@app.get("/")
async def home():
    return {"msg":"Hello all Employees good morning"}

@app.get("/get_all_departments",response_model = list[GetDepartment])
async def get_all_departments(db:Session=Depends(get_db)):
    get_all_departments = db.query(Department).all()
    return get_all_departments

@app.post("/create_dept",response_model=GetDepartment)
async def create_department(dept:CreateDepartment,db:Session=Depends(get_db)):
    department_obj=Department(**dept.model_dump())
    db.add(department_obj)
    db.commit()
    db.refresh(department_obj)
    return department_obj

class CreateEmp(BaseModel):
    name:str
    dept_id:Optional[int] = None
    email_id:EmailStr
    salary:int
    joining_date:date

class GetEmployess(BaseModel):
    id:int
    name:str
    dept_id:Optional[int] = None
    salary:int
    email_id:EmailStr
    joining_date:date
    updated_at:datetime

    class Config:
        from_attributes = True


@app.post("/create_emp",response_model=GetEmployess)
async def create_emp(emp:CreateEmp,db:Session=Depends(get_db)):
    emp_obj=Employee(**emp.model_dump())
    db.add(emp_obj)
    db.commit()
    db.refresh(emp_obj)
    return emp_obj
@app.get("/get_emp",response_model=list[GetEmployess])
async def get_employees(db:Session=Depends(get_db)):
    emp_obj = db.query(Employee).all()
    return emp_obj

class UpdateEmp(BaseModel):
    name:Optional[str] = None
    email_id :Optional[EmailStr] = None
    salary:Optional[int] = None
    joining_date:Optional[date]=None

class EmployeeResponse(BaseModel):
    msg:str
    Data:GetEmployess

@app.patch("/update_emp/{emp_id}",response_model=EmployeeResponse)
async def update_emp(emp_id:int,updateemp:UpdateEmp,db:Session=Depends(get_db)):
    get_emp = db.query(Employee).filter(Employee.id==emp_id).first()
    if get_emp:
        update_data = updateemp.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            setattr(get_emp,key,value)
        db.commit()
        db.refresh(get_emp)
        return {"msg":"Employee Updated Successfully","Data":get_emp}
    else:
        raise HTTPException(status_code=404,detail="Employee not found")
@app.get("/search_emp",response_model=list[GetEmployess])   
async def search_emp(
        emp_id:Optional[int]=Query(None),
        name:Optional[str]=Query(None),
        email_id:Optional[EmailStr]=Query(None),
        db:Session=Depends(get_db)):
    query = db.query(Employee)
    if email_id:
        query=query.filter(Employee.email_id==email_id)
    if name:
        query=query.filter(Employee.name.ilike(f"%{name}%"))
    if emp_id:
        query =query.filter(Employee.id==emp_id)
    if query:
        return query.all()
    raise HTTPException(status_code=404,detail="Employee not found")

@app.delete("/delete_emp/{emp_id}")
async def delete_emp(emp_id:int,db:Session=Depends(get_db)):
    emp=db.query(Employee).filter(Employee.id==emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
        return {"msg":"Employee deleted successfully"}
    raise HTTPException(status_code=404,detail="Employee not found")

class GetNth(BaseModel):
    id:int
    name:str
    salary:int
    sal_rank:int
    dept_name:str
    
    class Config:
        from_attributes = True
@app.get("/get_nth_higest_emp/{rank}",response_model=list[GetNth])
async def get_nth_highest_emp(rank:int,db:Session=Depends(get_db)):
    subquery = (
        db.query(Employee.id,Employee.name,Department.name.label("dept_name"),Employee.salary,func.dense_rank().over(
            partition_by=Employee.dept_id,order_by=Employee.salary.desc()).label("sal_rank")
                 ).join(Department,Employee.dept_id==Department.id)
    ).subquery()

    result = db.query(subquery).filter(subquery.c.sal_rank==rank).all()
    return result
