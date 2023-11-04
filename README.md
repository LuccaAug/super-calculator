# Super Calculator
Group: Lucca Augusto

## About
The Super-Calculator is a calculator for various formulas in only one place,
it has formulas for physic, trigonometric, computation and medicine.

You can calculate the speed of Max Verstappen, your grandpa BMI or the sine of 0.


## Technical Specifications
### Development
The program was developed to use only standard packages, it uses:
* **abc** to mark abstract methods in the base classes
* **math** to the formulas that needs complex mathematics functions
* **unittest** to develop the unit tests

To make better reports it uses **coverage** and **lizard**, as specified in _requirements.txt_


### GitHub Actions
The GitHub Actions was set to create a specific environment, to avoid version problems, it does the steps below:
1. Install a specific version of python
2. Install the packages of _requirements.txt_ (**coverage** and **lizard**)
3. Runs the tests with **coverage**
4. Shows the **coverage** report
5. Shows the **lizard** report for the files excluding the tests
