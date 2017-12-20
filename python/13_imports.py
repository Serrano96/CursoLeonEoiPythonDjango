import utils

utils.libMethod()

from libs import bombing

bombing.where_are_the_bombs()

from libs.bombing import where_are_the_bombs as where()
where()

from libs.eating import *
eat_apples(5)