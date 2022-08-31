// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

// @title Contract to agree on the lunch venue
contract land_contract {
    struct Land {
        string land_hash; // only for debugging purposes.
        string location;
        address payable owner_addr; bool for_sale;
        uint value_in_ether; // price of land
    }

    mapping (string => Land) public lands;
    uint public num_lands = 0;

    address public owner;
    constructor () {
        owner = msg.sender;
    }

    modifier is_owner {
        require(msg.sender == owner, "Must be owner of contract.");
        _;
    }

    modifier is_land_owner(string memory land_hash) {
        require(msg.sender == lands[land_hash].owner_addr, "Can only be done by landowner.");
        _;
    }

    // Only allow oracle to call this function.
    function land_register(
        string memory land_hash,
        string memory location,
        address payable owner_addr
    ) external is_owner {
        Land memory l;
        l.land_hash = land_hash;
        l.location = location;
        l.owner_addr = owner_addr;
        l.for_sale = false;
        l.value_in_ether = 0;

        lands[land_hash] = l;
        num_lands++;
    }

    function view_land(string memory land_hash) view public
    returns (
        string memory,
        string memory,
        address,
        bool,
        uint
    ) {
        return (
            lands[land_hash].land_hash,
            lands[land_hash].location,
            lands[land_hash].owner_addr,
            lands[land_hash].for_sale,
            lands[land_hash].value_in_ether
        );
    }

    function put_land_on_sale(string memory land_hash, uint ether_price) public is_land_owner(land_hash) {
        lands[land_hash].for_sale = true;
        lands[land_hash].value_in_ether = ether_price;
    }

    function buy_land(string memory land_hash) payable public {
        require(msg.value == to_ether(lands[land_hash].value_in_ether), "Not enough ether to buy this land!");
        lands[land_hash].owner_addr.transfer(to_ether(lands[land_hash].value_in_ether));
        lands[land_hash].owner_addr = payable(msg.sender);
        lands[land_hash].for_sale = false;
    }

    function to_ether(uint value_in_ether) public pure returns (uint) {
        return value_in_ether * (1 ether);
    }
}
