from pydantic import BaseModel, Field
from typing import Annotated

class CustomerData(BaseModel):

    gender: Annotated[int, Field(..., ge=0, le=1, description="Customer gender: Male=1, Female=0")]
    SeniorCitizen: Annotated[int, Field(..., ge=0, le=1, description="Whether the customer is a senior citizen (1=Yes, 0=No)")]
    Partner: Annotated[int, Field(..., ge=0, le=1, description="Customer has a partner (1=Yes, 0=No)")]
    Dependents: Annotated[int, Field(..., ge=0, le=1, description="Customer has dependents (1=Yes, 0=No)")]
    
    tenure: Annotated[int, Field(..., ge=0, description="Number of months the customer has stayed with the company")]

    PhoneService: Annotated[int, Field(..., ge=0, le=1, description="Customer has phone service (1=Yes, 0=No)")]
    MultipleLines: Annotated[int, Field(..., ge=0, le=1, description="Customer has multiple phone lines (1=Yes, 0=No)")]
    
    OnlineSecurity: Annotated[int, Field(..., ge=0, le=1, description="Customer has online security service (1=Yes, 0=No)")]
    OnlineBackup: Annotated[int, Field(..., ge=0, le=1, description="Customer has online backup service (1=Yes, 0=No)")]
    DeviceProtection: Annotated[int, Field(..., ge=0, le=1, description="Customer has device protection service (1=Yes, 0=No)")]
    TechSupport: Annotated[int, Field(..., ge=0, le=1, description="Customer has tech support service (1=Yes, 0=No)")]
    
    StreamingTV: Annotated[int, Field(..., ge=0, le=1, description="Customer has streaming TV service (1=Yes, 0=No)")]
    StreamingMovies: Annotated[int, Field(..., ge=0, le=1, description="Customer has streaming movies service (1=Yes, 0=No)")]
    
    PaperlessBilling: Annotated[int, Field(..., ge=0, le=1, description="Customer uses paperless billing (1=Yes, 0=No)")]
    
    MonthlyCharges: Annotated[float, Field(..., ge=0, description="Monthly amount charged to the customer")]
    TotalCharges: Annotated[float, Field(..., ge=0, description="Total amount charged to the customer")]

    InternetService_Fiber_optic: Annotated[int, Field(..., ge=0, le=1, description="Customer uses fiber optic internet (1=Yes, 0=No)")]
    InternetService_No: Annotated[int, Field(..., ge=0, le=1, description="Customer has no internet service (1=Yes, 0=No)")]
    
    Contract_One_year: Annotated[int, Field(..., ge=0, le=1, description="Customer has one-year contract (1=Yes, 0=No)")]
    Contract_Two_year: Annotated[int, Field(..., ge=0, le=1, description="Customer has two-year contract (1=Yes, 0=No)")]
    
    PaymentMethod_Credit_card: Annotated[int, Field(..., ge=0, le=1, description="Payment method is credit card (1=Yes, 0=No)")]
    PaymentMethod_Electronic_check: Annotated[int, Field(..., ge=0, le=1, description="Payment method is electronic check (1=Yes, 0=No)")]
    PaymentMethod_Mailed_check: Annotated[int, Field(..., ge=0, le=1, description="Payment method is mailed check (1=Yes, 0=No)")]