function calcCapacitance(input) {
	band1_val = document.bandSelect.band1.value;
	console.log(band1_val)
	band2_val = document.bandSelect.band2.value;
	mult = document.bandSelect.band3.value;
	tol = document.bandSelect.band4.value;
	volt = document.bandSelect.band5.value;
	volt = volt
	if (band1_val === "0") {
		band1_val = "";
	}
	if (volt == "0") {
		volt = " ";
	}
	capcitorText = band1_val + band2_val; // Appends two strings
	for (var i = 0; i < mult; i++) {
		capcitorText += "0";  // Append some 0's
	}
	capcitorText += " \pF \u00B1 " + tol; // Add ohm, space, plus/minus sign

	document.getElementById("capacitorValue").innerHTML = capcitorText;
	document.getElementById("capacitorVoltage").innerHTML = volt;
}

function addCommas(x) {
	// This handy function found here:
	// http://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript
	return x.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
