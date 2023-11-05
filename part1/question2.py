################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`


def swapper(tupla):
      """
  Intercambia los dos elementos de una tupla de dos elementos.

  Args:
    tupla: La tupla de dos elementos a intercambiar.

  Returns:
    Una tupla con los dos elementos intercambiados.
  """

  # Versión con la función `::-1`

  tupla = tupla[::-1]

  return tupla


def run_swapper(tupla):
  """
  Ejecuta la función `swapper` con la tupla proporcionada.

  Args:
    tupla: La tupla a intercambiar.

  Returns:
    La tupla intercambiada.
  """

  tupla_intercambiada = swapper(tupla)

  return tupla_intercambiada


if name == "main":
  tupla = ("a", "b")

  tupla_intercambiada = run_swapper(tupla)

  print(tupla_intercambiada)
