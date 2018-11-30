from guc_overflow.permissions import IsObjectOwner


class IsProfileOwner(IsObjectOwner):
    """
    Object-level permission to allow profile owner only
    to make changes to the object.

    Author: Abdelrahmen Ayman
    """
    pass
