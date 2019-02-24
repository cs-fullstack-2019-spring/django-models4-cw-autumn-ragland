### POINTS: 2
### KEY: Fine job! A little morbid, but still good :-P

# Django Models and Foreign keys

### Exercise 1

Create a model called ```Mom``` with ```mom_first_name```, ```mom_last_name```, and ```mom_phone_number```.

Create a second model called ```Child``` with ```child_first_name```, ```child_last_name```, and ```child_mom``` that is a ForeignKey that references ```Mom``` (deleting a Mom SHOULD delete all of their children)

Add 3 Moms using the Django Admin console

Add 3 Children using the Django Admin console

Assign 1 Child to each Mom using the Django Admin console

Add an endpoint ```children/``` that will list all Children and their Mom by Child

Add an endpoint ```moms/``` that will list all Moms and their Children by Mom

Add an endpoint ```addchild/``` that will add a Child to each Mom

Add an endpoint ```deletemom/``` that will delete the first Mom and all of their their Children

Confirm changes by using the ```children/``` and ```moms/``` endpoints


### Exercise 2
Create a model called ```State``` with ```state_name```.

Create a model called ```Citizen``` with ```citizen_first_name```, ```citizen_last_name```. and ```citizen_state``` that is a ForeignKey that references ```State``` (deleting a Citizen should NOT delete corresponding state)

Add KY, TN, and MS to states using the Django Admin console.

Add 3 citizens using the Django Admin console and assign your first Citizen to ```TN``` and the other 2 Citizens to ```KY```

Add an endpoint ```citizens/``` that will list all Citizens and their States

Add an endpoint ```chgstate/``` that will change the State of the last Citizen from ```KY``` to ```MS```

Confirm changes by using the ```citizens/``` endpoint

