def collision(object1, object2):
     if (object2.x + object2.widht >= object1.x >= object2.x or object1.x + object1.width >= object2.x >= object1.x) and (object2.y + object2.height >= object1.y >= object2.y or object1.y + object1.height >= object2.y >= object1.y):
        return True
