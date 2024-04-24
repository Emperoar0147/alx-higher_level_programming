#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
    if (err) {
        console.error(`Error reading ${sourceFile1}: ${err.message}`);
        return;
    }

    // Read the content of the second source file
    fs.readFile(sourceFile2, 'utf8', (err, data2) => {
        if (err) {
            console.error(`Error reading ${sourceFile2}: ${err.message}`);
            return;
        }

        // Concatenate the content of the two source files
        const concatenatedData = data1 + data2;

        // Write the concatenated content to the destination file
        fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
            if (err) {
                console.error(`Error writing to ${destinationFile}: ${err.message}`);
                return;
            }
            console.log(`Concatenated data has been written to ${destinationFile}`);
        });
    });
});
