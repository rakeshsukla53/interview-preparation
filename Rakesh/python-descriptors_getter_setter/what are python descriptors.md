
# why we use property 

it is just a way to create readonly properties. 

In this example i want to make the name property as readonly so the way do that either you can define the 
name variable as `__name` as no one can access that from outside or you can define the `@property` for it so that you no on access from outside.

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Rakesh/python-descriptors_getter_setter/decorators_getter_setter.png)

Take this example of a Bank Account, you don't want anyone to access the attribute `balance` because then anyone can see the balance amount. So we have defined it as `__name` so it can be used outside of the class. The way to read the retrieve or change the value is by `getter` and `setter` function

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Rakesh/python-descriptors_getter_setter/access_private_variables_using_getter_setter.png)

