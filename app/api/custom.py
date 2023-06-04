from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import schema, service
from app.db.session import get_db

router = APIRouter()


@router.get('/feature', response_model=schema.ResponseCanAccess,
            responses={
                404: {
                    "description": "Feature access not found."
                },
            },
            )
def get_can_user_access_feature(
    email: str,
    featureName: str,
    db: Session = Depends(get_db),
):
    """
    Check if the user can access the feature.

    - **email**: User's email. E.g. thomas@gmail.com
    - **featureName**: Feature name. E.g. Dark theme UI
    """

    feature_access = service.get_feature_access(
        db=db,
        user_email=email,
        feature_name=featureName,
    )

    if feature_access == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Feature access not found.")

    return schema.ResponseCanAccess(
        canAccess=feature_access.is_enabled
    )


@router.post('/feature', status_code=status.HTTP_200_OK,
             responses={
                 200: {
                     "description": "Updated successfully.",
                     "content": None
                 },
                 304: {
                     "description": "Failed to update."
                 },
             },
             )
def update_access_feature(
    req: schema.RequestUpdateFeatureAccess,
    db: Session = Depends(get_db),
):
    """
    Update the feature access of the user.

    Example request body:
    ```json
    {
        "featureName": "Dark theme UI",
        "email": "thomas@gmail.com",
        "enable": true
    }
    ```
    """

    feature = service.update_feature_access(
        db=db,
        req_feature_access=req,
    )

    if feature == None:
        return Response(status_code=status.HTTP_304_NOT_MODIFIED)

    return Response(status_code=status.HTTP_200_OK)
