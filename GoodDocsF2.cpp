//: GoodDocs.cpp

/* 
 Title: GoodDocsF.cpp
 Description: Temperature Conversion Program
 Date: December 8, 2013
 Author: Richard S. Huntrods
 Version: 1.0
 Copyright: 2013 Richard S. Huntrods
 
 
 Editied by Nathan Prasad For COM 200 Project 1
 April 21, 2020 
 renamed to GoodDocsF2.cpp for submission purposes.
 
 Formulas corrected at lines 53 and 71, Brackets adjusted accordingly 
 
*/


#include <iostream> // Stream declarations
using namespace std;

int main(void) {
	char input_units, output_units;
	float input_temp, output_temp;
	int error = 0;

	// request and obtain name
	cout << "What is the input temperature? ";
	cin >> input_temp;

	// request and obtain age
	cout << "What are the units of the input temperature (C for Celcius or F for Fahrenheit)? ";
	cin >> input_units;

	// convert input units to upper case
	input_units = toupper(input_units);

	// check input_units for acceptable response; perform appropriate conversion if acceptable and print error message if not
	if(input_units == 'C') {
		// display input
		cout << "Your input temperature is " << input_temp << input_units;

		// range check input_temp
		if(input_temp < -273) {
			// disply out of range error message
			cout << " which is out of range (less than -273C or -416F)." << endl;
		}
		else {
			// convert from Celcius to Fahrenheit
			output_units = 'F';
			output_temp = (input_temp * 9.0 / 5.0) + 32;

			// display converted output
			cout << " which is " << output_temp << output_units << "." << endl;
		}
	}
	else if(input_units == 'F') {
		// display input
		cout << "Your input temperature is " << input_temp << input_units;

		// range check input_temp
		if(input_temp < -416) {
			// out of range
			cout << " which is out of range (less than -273C or -416F)." << endl;
		}
		else {
			// convert from Fahrenheit to Celcius
			output_units = 'C';
			output_temp = (input_temp - 32.0) * 5.0 / 9.0;

			// display converted output
			cout << " which is " << output_temp << output_units << "." << endl;
		}
	}
	else {
		// display input_unit error message
 		cout << "The units you have specified are not one of C (Celcius) or F (Fahrenheit)" << endl;
	}
} ///:~