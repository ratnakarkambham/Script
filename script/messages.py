from enum import Enum
from rest_framework import status

class Messages(Enum):
    success = ( "Success", status.HTTP_200_OK)
    batchUploadSuccess = ("Batch Uploaded Successfully", status.HTTP_200_OK)
    insertSuccess = ("Insert success", status.HTTP_201_CREATED)
    updateSuccess = ("Update success", status.HTTP_200_OK)
    deleteSuccess = ("Delete success", status.HTTP_204_NO_CONTENT)
    notAuthenticated = ("Invalid username or password", status.HTTP_401_UNAUTHORIZED)
    notAuthorized = ("No permission", status.HTTP_403_FORBIDDEN)
    severeError = ("Severe error", status.HTTP_500_INTERNAL_SERVER_ERROR)
    testPass = ("Test success", status.HTTP_200_OK)
    testFail = ("Test fail", status.HTTP_500_INTERNAL_SERVER_ERROR)
    notFound = ("No data found, please contact support", status.HTTP_404_NOT_FOUND)
    sqlerror = ("Data Error, please contact support", status.HTTP_400_BAD_REQUEST)
    serialize_err=("Data serialization failed",status.HTTP_422_UNPROCESSABLE_ENTITY )
    screenplayNotFound = ("Screenplay does not exist", status.HTTP_404_NOT_FOUND)
    emotionsNotFound = ("Emotion Analytics not found", status.HTTP_404_NOT_FOUND)
    charactersNotFound = ("No characters found", status.HTTP_404_NOT_FOUND)
    genderNotFound = ("Gender data not found", status.HTTP_404_NOT_FOUND)
    genreNotFound = ("Genre data not found", status.HTTP_404_NOT_FOUND)
    processFail = ("PDF Processing failed", status.HTTP_422_UNPROCESSABLE_ENTITY )
    BA00 = ("BA00 - PDF has image elements", status.HTTP_422_UNPROCESSABLE_ENTITY )
    BA01 = ("BA01 - PDF has invalid format, or is a scanned copy with images of text", status.HTTP_422_UNPROCESSABLE_ENTITY )
    BA02 = ("BA02 - PDF Processing failed", status.HTTP_422_UNPROCESSABLE_ENTITY )
    BA03 = ("BA03 - Invalid username; severe error, contact support", status.HTTP_401_UNAUTHORIZED )
    BA04 = ("BA04 - Support for this language will come soon", status.HTTP_404_NOT_FOUND)
    BA05 = ("BA05 - Transliteration failed", status.HTTP_422_UNPROCESSABLE_ENTITY)
    usernameFail=("Username taken",status.HTTP_422_UNPROCESSABLE_ENTITY )
    emailFail=("Email invalid or taken",status.HTTP_422_UNPROCESSABLE_ENTITY )
    emailNotFound=("Email not found in our system",status.HTTP_400_BAD_REQUEST )
    otpExpire=("OTP has expired",status.HTTP_422_UNPROCESSABLE_ENTITY )
    otpInvalid=("OTP is invalid",status.HTTP_422_UNPROCESSABLE_ENTITY )
    passwordInvalid=("Current password is invalid",status.HTTP_400_BAD_REQUEST )
    emailSendFail=("Email send failed for: {}",status.HTTP_422_UNPROCESSABLE_ENTITY )
    signupFail=("Signup failed, please contact support",status.HTTP_422_UNPROCESSABLE_ENTITY )
    invalidClient=("Invalid client found, please contact support",status.HTTP_422_UNPROCESSABLE_ENTITY )
    gmailSigninFail=("Gmail sign-in failed, please contact support",status.HTTP_422_UNPROCESSABLE_ENTITY )
    getSubsriptionError=("Error in fetching subscription details",status.HTTP_422_UNPROCESSABLE_ENTITY )
    getProfileError=("Error in fetching profile details",status.HTTP_422_UNPROCESSABLE_ENTITY )
    presignedurlGenerationFailed = ("DN01",status.HTTP_422_UNPROCESSABLE_ENTITY )
    visitorAddFailed = ("VS01", status.HTTP_422_UNPROCESSABLE_ENTITY )
    severeLoginError = ("Login should not have failed, please contact support", status.HTTP_422_UNPROCESSABLE_ENTITY )