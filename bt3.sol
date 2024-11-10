pragma solidity ^0.8.26;
contract Demo {
uint private newbal = 3500;
function deposit(uint x) public {
newbal += x;
}
function withdraw(uint x) public {
if (newbal < x) {
revert("Insufficient balance");
}
newbal -= x;
}
function show() public view returns (uint) {
return newbal;
}
}


// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract BankAccount {
    mapping(address => uint) private balances; // Each user's balance

    // Deposit function
    function deposit(uint amount) public {
        balances[msg.sender] += amount; // Update sender's balance
    }

    // Withdraw function
    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance"); // Check if sender has enough balance
        balances[msg.sender] -= amount; // Update sender's balance
    }


    This Solidity contract is a simple implementation of a bank account system with three main functions: deposit, withdraw, and show balance.

Breakdown:
State Variables:

mapping(address => uint) private balances;: This mapping stores the balance for each user, identified by their Ethereum address.
Deposit Function:

function deposit(uint amount) public { ... }: This function allows a user to deposit a specified amount into their account. The deposit is added to the sender's balance.
balances[msg.sender] += amount;: Updates the sender's balance with the deposited amount.
Withdraw Function:

function withdraw(uint amount) public { ... }: This
require(balances[msg.sender] >= amount, "Insufficient balance");: Us
balances[msg.sender] -= amount;:
Show Balance Function:

function showBalance() public view returns (uint) { ... }: This function
return balances[msg.sender];: It returns the sender's balance.
Key Points:
The contract uses the msg.sender to track each user's address and manage their balance.
The requirestatementwithdrawfunction
The deposit and withdraw functions are straightforward and modify the balances stored in the mapping.
Use Case:
Users can deposit and withdraw funds from their accounts, ensuring that only the account owner can access and modify their balance. The contract does not include additional features like interest rates or transaction fees, making it a simple implementation of a bank account.







    // Show balance function
    function showBalance() public view returns (uint) {
        return balances[msg.sender]; // Return sender's current balance
    }
}
