def sponge():
    """This function is the guide for the q-arm to pick up the sponge and bring it to the drop box and output to the user that the sponge has been packed.

    This function was done by: Team."""

    arm.rotate_base(-2) # aligns itself with the sponge
    sleep(1)

    arm.set_arm_position([0.5738982662177072, 0.15743862479559878, 0.09944466639331564]) # Goes to the sponge position
    sleep(1)

    arm.rotate_gripper(180) # Closes the gripper (clamps the item)
    sleep(1)
    arm.rotate_elbow(-30) # rotates the arm up in order to avoid hitting objects in the way
    sleep(1)

    arm.set_arm_position([0.18979054455766792, -0.3173793004837362, 0.26387376367500665]) # goes to the drop box position
    sleep(1)

    arm.rotate_gripper(-45) #opens the gripper to release the object
    sleep(1)
    print("Sponge has been packed!")

def bottle():

    """This function is the guide for the q-arm to pick up the bottle and bring it to the drop box and output to the user that the bottle has been packed.

    This function was done by: Team."""

    arm.rotate_base(-1) # aligns itself with the bottle
    sleep(1)

    arm.set_arm_position([0.603889673157745, 0.08439876809693939, 0.11711224137045179]) # Goes to the bottle position
    sleep(1)

    arm.rotate_gripper(180) # Closes the gripper (clamps the item)
    sleep(1)
    arm.rotate_elbow(-30) # Rotates the arm up in order to avoid hitting objects in the way
    sleep(1)

    arm.set_position([0.18979054455766792, -0.3173793004837362, 0.26387376367500665]) # goes to the drop box position
    sleep(1)

    arm.rotate_gripper(-45) #opens the gripper to release the object
    sleep(1)
    print("Bottle has been packed!")

def rook():
    """This function is the guide for the q-arm to pick up the rook and bring it to the drop box and output to the user that the rook has been packed.

    This function was done by: Team."""

    arm.rotate_base(2) # aligns itself with the rook
    sleep(1)

    arm.set_position([0.5911439372738108, 0.01678446857857702, 0.052937878438266694]) # Goes to the rook
    sleep(1)

    arm.rotate_gripper(180) # Closes the gripper (clamps the item)
    sleep(1)
    arm.rotate_elbow(-30) # Rotates the arm up in order to avoid hitting objects in the way
    sleep(1)

    arm.set_position([0.18979054455766792, -0.3173793004837362, 0.26387376367500665]) # goes to the drop box position
    sleep(1)

    arm.rotate_gripper(-45) #opens the gripper to release the object
    sleep(1)
    print("Rook has been packed!")

def d12():
    """This function is the guide for the q-arm to pick up the d12 and bring it to the drop box and output to the user that the d12 has been packed.

    This function was done by: Team."""

    arm.rotate_base(3) # alings itself with the d12
    sleep(1)

    arm.set_position([0.6017113834020855, -0.03280744043874341, 0.0659842280292641])  # Goes to the d12
    sleep(1)

    arm.rotate_gripper(180) # Closes the gripper (clamps the item)
    sleep(1)
    arm.rotate_elbow(-30) # Rotates the arm up in order to avoid hitting objects in the way
    sleep(1)

    arm.set_position([0.18979054455766792, -0.3173793004837362, 0.26387376367500665]) # goes to the drop box position
    sleep(1)

    arm.rotate_gripper(-45) #opens the gripper to release the object
    sleep(1)
    print("d12 has been packed!")

def witchHat():
    """This function is the guide for the q-arm to pick up the witch hat and bring it to the drop box and output to the user that the witch hat has been packed.

    This function was done by: Team."""

    arm.rotate_base(5) # aligns itself with the witch hat
    sleep(1)

    arm.set_position([0.5913819533576008, -0.11248303136361129, 0.038436410892180445]) #Goes to the witch hat
    sleep(1)

    arm.rotate_gripper(180) # Closes the gripper (clamps the item)
    sleep(1)
    arm.rotate_elbow(-30) # Rotates the arm up in order to avoid hitting objects in the way
    sleep(1)

    arm.set_position([0.18979054455766792, -0.3173793004837362, 0.26387376367500665]) # goes to the drop box position
    sleep(1)

    arm.rotate_gripper(-45) #opens the gripper to release the object
    sleep(1)
    print("Witch Hat has been packed!")

def bowl():
    """This function is the guide for the q-arm to pick up the bowl and bring it to the drop box and output to the user that the bowl has been packed.

    This function was done by: Team."""

    arm.rotate_base(6) # aligns itself with the bowl
    sleep(1)

    arm.set_position([0.5841038305383393, -0.17870096857920106, 0.05034593933181705])  #Goes to the bowl
    sleep(1)

    arm.rotate_gripper(180) # Closes the gripper (clamps the item)
    sleep(1)
    arm.rotate_elbow(-30) # rotates the arm up in order to avoid hitting objects in the way
    sleep(1)

    arm.set_position([0.18979054455766792, -0.3173793004837362, 0.26387376367500665]) # goes to the drop box position
    sleep(1)

    arm.rotate_gripper(-45) # opens the gripper to release the object
    sleep(1)
    print("Bowl has been packed!")

def pack_products(product_list):

    """This function takes the product_list as a parameter and then the program checks if there is an invalid item in the parameter, if not, it iterates through the list of items and goes to the item, picks it up, and drops it off at the drop box, and outputs to the user that the item has been packed.

    This function was done by: Team."""

    counter = 0
    items = ["Sponge", "Bottle", "Rook", "D12", "WitchHat", "Bowl"] # list of the valid items

    for i in range (len(product_list)): # iterates through the product_list to check if any of the items are invalid
        if not product_list[i][0] in items:
            print("Invalid input!")
            counter = 1
            break

    if counter == 0: # if all of the items in the product_list are valid
        for i in range (len(product_list)): # iterates through all of the items in the product list

            arm.home() # Brings it back home

            arm.rotate_gripper(180) # closes the gripper fully
            sleep(1)

            arm.rotate_gripper(-80) #Opens the end effector
            sleep(1)

            if product_list[i][0] == items[0]: # Checks if the product is a sponge
                sponge()

            elif product_list[i][0] == items[1]: # Checks if the product is a bottle
                bottle()

            elif product_list[i][0] == items[2]: # Checks if the product is a rook
                rook()

            elif product_list[i][0] == items[3]: # Checks if the product is a D12
                d12()

            elif product_list[i][0] == items[4]: # Checks if the product is a WitchHat
                witchHat()

            elif product_list[i][0] == items[5]: # Checks if the product is a bowl
                bowl()
