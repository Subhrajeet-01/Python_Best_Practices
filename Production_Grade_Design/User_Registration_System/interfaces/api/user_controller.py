from fastapi import APIRouter, HTTPException
from domain.exceptions import UserAlreadyExistsException, InvalidEmailException
from application.dto import RegisterUserRequest
from application.use_cases.register_user import RegisterUser

router = APIRouter()

def register_routes(use_case: RegisterUser) -> APIRouter:

    @router.post("/users")
    def register_user(request: dict):
        try:
            dto = RegisterUserRequest(request["email"])
            user = use_case.execute(dto)
            return {"email": user.email}
        
        except UserAlreadyExistsException as e:
            raise HTTPException(409, "User already exists.")
        
        except InvalidEmailException as e:
            raise HTTPException(400, "Invalid email provided.")
        
        except ValueError as e:
            raise HTTPException(400, str(e))

    return router