
from pydantic import BaseModel


class ProcessResponse(BaseModel):
    is_fraud: bool
    blood_pressure_evidences: list
    heart_rate_evidences: list

    @staticmethod
    def serialize(is_fraud, blood_pressure_evidences, heart_rate_evidences):
        return {
            'is_fraud': is_fraud,
            'blood_pressure_evidences': blood_pressure_evidences,
            'heart_rate_evidences': heart_rate_evidences
        }
