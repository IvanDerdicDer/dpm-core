# Introduction

Database Permission Manager (**DPM**) is a program inspired by [DBT](https://www.getdbt.com/) and 
[Terraform](https://www.terraform.io/).
The aim of this project is to create a CICD friendly program for managing database permissions.
As it is inspired by DBT the project contains multiple components. 
Each component deals with a specific database.

# Current scope
Current scope of the project is to develop permission management on database, schema, 
and table level for users and roles. This also means DPM will create users and roles, but it will not 
create databases, schemas, and roles.

# dpm-core
Component dpm-core handles program execution and provides abstract dataclasses for other components.