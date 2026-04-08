// Task 2: JavaScript Implementation
class WeatherSystem {
    // Converted from Java
    checkStatus(temp) {
        return temp > 35 ? "Extreme Heat" : "Normal";
    }

    // Task 1's "Strong" function logic
    isStrong(windSpeed) {
        return windSpeed > 50; 
    }
}

// TDD Assertions for the "Strong" function
function runTests() {
    const ws = new WeatherSystem();
    const tests = [
        { val: 60, expected: true },
        { val: 40, expected: false },
        { val: 51, expected: true },
        { val: 50, expected: false },
        { val: 100, expected: true },
        { val: 0, expected: false },
        { val: -10, expected: false },
        { val: 50.1, expected: true }
    ];

    console.log("--- TDD Test Results ---");
    tests.forEach((t, i) => {
        const result = ws.isStrong(t.val);
        console.assert(result === t.expected, `Test ${i+1} Failed!`);
        console.log(`Test ${i+1}: ${result === t.expected ? "✅ Pass" : "❌ Fail"}`);
    });
}

runTests();