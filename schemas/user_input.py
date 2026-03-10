from pydantic import BaseModel, Field, computed_field
from typing import Annotated

class UserInput(BaseModel):

    gender: Annotated[int, Field(..., ge=0, le=1, description="Gender of customer (Male=1, Female=0)")]
    SeniorCitizen: Annotated[int, Field(..., ge=0, le=1, description="Whether the customer is a senior citizen")]
    Partner: Annotated[int, Field(..., ge=0, le=1, description="Customer has a partner")]
    Dependents: Annotated[int, Field(..., ge=0, le=1, description="Customer has dependents")]
    
    tenure: Annotated[int, Field(..., ge=0, description="Number of months customer has stayed with the company")]

    PhoneService: Annotated[int, Field(..., ge=0, le=1, description="Customer has phone service")]
    MultipleLines: Annotated[int, Field(..., ge=0, le=1, description="Customer has multiple phone lines")]

    OnlineSecurity: Annotated[int, Field(..., ge=0, le=1, description="Customer has online security service")]
    OnlineBackup: Annotated[int, Field(..., ge=0, le=1, description="Customer has online backup service")]
    DeviceProtection: Annotated[int, Field(..., ge=0, le=1, description="Customer has device protection service")]
    TechSupport: Annotated[int, Field(..., ge=0, le=1, description="Customer has tech support service")]

    StreamingTV: Annotated[int, Field(..., ge=0, le=1, description="Customer has streaming TV service")]
    StreamingMovies: Annotated[int, Field(..., ge=0, le=1, description="Customer has streaming movies service")]

    PaperlessBilling: Annotated[int, Field(..., ge=0, le=1, description="Customer uses paperless billing")]

    MonthlyCharges: Annotated[float, Field(..., ge=0, description="Monthly charges of the customer")]
    TotalCharges: Annotated[float, Field(..., ge=0, description="Total charges paid by the customer")]

    InternetService_Fiber_optic: Annotated[int, Field(..., ge=0, le=1, description="Customer uses fiber optic internet")]
    InternetService_No: Annotated[int, Field(..., ge=0, le=1, description="Customer has no internet service")]

    Contract_One_year: Annotated[int, Field(..., ge=0, le=1, description="Customer has one year contract")]
    Contract_Two_year: Annotated[int, Field(..., ge=0, le=1, description="Customer has two year contract")]

    PaymentMethod_Credit_card: Annotated[int, Field(..., ge=0, le=1, description="Payment method is credit card")]
    PaymentMethod_Electronic_check: Annotated[int, Field(..., ge=0, le=1, description="Payment method is electronic check")]
    PaymentMethod_Mailed_check: Annotated[int, Field(..., ge=0, le=1, description="Payment method is mailed check")]

    @computed_field
    @property
    def avg_monthly_spend(self) -> float:
        if self.tenure == 0:
            return 0
        return self.TotalCharges / self.tenure

    @computed_field
    @property
    def service_count(self) -> int:
        return (
            self.OnlineSecurity +
            self.OnlineBackup +
            self.DeviceProtection +
            self.TechSupport +
            self.StreamingTV +
            self.StreamingMovies
        )