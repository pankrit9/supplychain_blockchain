// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract register_oracle {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    event request_land_event(string land_hash, address land_owner);

    function request_land_register(string memory land_hash) public {
        // Send to blockchain listener: land_listener.py.
        emit request_land_event(land_hash, msg.sender);
    }
}
