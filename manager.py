from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True
    
    def create_user(self, email, password=None):    
            if not email:
                raise ValueError('Email is mandatory')
            user=self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save(using=self._db)
            return user
        
    def create_superuser(self, email, password,**kwargs):
        if password is None:
            raise TypeError("provide password please")
        user = self.create_user(
            email,
            password=password,
            **kwargs)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
    
        return user


       #
    #def create_staffuser(self, email, password):
     #   user = self.create_user(
     #       email,
     #       password=password,
     #   )
     #   user.staff = True
     #   user.save(using=self._db)
      #  return user
       #  
        