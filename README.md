# Blockchain-Based Land Title Management

## Overview
This project implements a blockchain-based system for land title management, addressing several challenges in the traditional land registry processes. By leveraging blockchain technology, the system aims to enhance transparency, security, and efficiency in land title management.

## Challenges in Traditional Land Title Management
- Centralization and Trust: Traditional systems are often centralized, leading to potential misuse of power and lack of public trust.
- Forgery: Paper-based land titles are prone to forgery and manipulation.
- Document Damage/Loss: Physical documents can be damaged or lost, leading to disputes and complications.
- Complexity: The conventional process involves complicated interactions with multiple government departments.
- Traceability: In many regions, tracing the history of land ownership is challenging.

## Blockchain Solution

Our blockchain-based solution addresses these challenges:

Decentralization: Removes centralized control, replacing trust with cryptographic verification.
Transparency and Security: Real-time verification of land ownership and transparent transaction history.
Digital Records: Digital documentation reduces risks of damage or loss.
Simplified Processes: Smart contracts automate and streamline transactions.
Traceability: A clear, accessible record of land ownership history.

## Functional and Non-Functional Requirements

### Functional:

Access to land information
Registration and transfer of land ownership
Partition sales among multiple owners
Off-chain storage of legal documents
Public/private key cryptography for transactions

### Non-Functional:

Availability: Web-based access on various devices
Data Integrity: Immutability of records
Latency: Quick transaction confirmations
Scalability: Performance with increasing demands
Security: Protection of identities and transactions

## Development Plan
Blockchain Platform: Ethereum
Off-Chain Components:
Oracle: Chain Link
Database: Cloud-based storage for land-related documents

## Domain Background

In many developing countries, the lack of a trusted and transparent land registry system poses significant challenges. With over 70% of the world’s population lacking legally registered land titles, blockchain technology offers a decentralized and secure solution to this problem.

## Implementation Details
Blockchain Platform: Ethereum
Database: Combination of blockchain and cloud storage
Hashing Algorithm: sha256sum for off-chain computations
User Interface: land_gui.py and land_listener.py for local hosting

## Conclusion

This project demonstrates the potential of blockchain technology in transforming land title management systems, especially in regions where traditional methods are fraught with challenges. Our solution aims to bring about a paradigm shift in how land titles are managed, making them more secure, transparent, and accessible.

## Notes:

- [IMPORTANT] All applications must be run in the root directory (i.e. NOT ./app/ or ./contracts).
For example, to run `land_gui.py`, the command would be `python3 app/land_gui.py`.
- Create a new branch, make commits and submit your merge requests (don't push
  directly to master!)
- Run `git pull` on the master branch before working, then `git checkout
  YOUR_BRANCH` and `git merge master` to always have a copy of the latest
  changes.


A typical first-time session with a new branch (e.g. `edit_readme_branch`) looks like:
```
$ git clone gitlab@gitlab.cse.unsw.EDU.AU:z5313514/comp6452_project_2.git
$ git checkout -b edit_readme_branch
### Create file(s), e.g. README.md and .gitignore ###
$ git add README.md .gitignore
$ git commit -m "Added typical session in README.md and imported .gitignore files for solidity"
$ git push -u origin edit_readme_branch 
### Follow the link outputted and submit the merge request using Gitlab web interface ###
```

Subsequent session on a branch that's already been created:
```
$ git checkout master
$ git pull
$ git checkout edit_readme_branch
$ git merge master
### Edit file(s), e.g. README.md and .gitignore ###
$ git add README.md .gitignore
$ git commit -m "Edited README.md and .gitignore"
$ git push
### Follow the link outputted and submit the merge request using Gitlab web interface ###
```
