# Ticket Interface
Stores and retrieves summary of JIRA tickets; solved as a code assignment

## Instructions
The customer wishes to build a system storing summary information about their
internal JIRA tickets.  In short, the system will:

- [ ] Receive POST notifications from JIRA
- [x] Store relevant fields from the notifications
- [x] If applicable, calculate the time between ticket created and ticket closed
- [x] Provide an ability to retrieve the records via a GET request.
 

Below is the sample payload containing only the fields of interest. 

```
{

  "summary" : "",

  "created": "2018-01-10T20:15:07.958Z",

  "completed": "", // Date time the ticket was closed.

  "description" : "",

  "priority" : "Major" 

}
```


### Technical limitations.  
* Must be implemented in Python and hosted as AWS Lambdas
* You must use DynamoDB as your datastore.

### Notes:
* Put all your region-specific resources in the US-West (Oregon) region
You do not need a real JIRA instance if you don’t have one readily available;
you can simulate the POST call however you wish

### Hints:
* Serverless Framework https://serverless.com/ (optional, but major extra credit
kudos)

* You will need to use more AWS services than mentioned above
 
### Submission
This project should be completable within the AWS free tier.  To submit the code
back to Turnberry:

- include a READ.me file in the Github repo that at least briefly
  lists/describes the AWS services you choose to use

---
## Design Plan
At the heart, the problem is of storing and reading data. So we are going to
figure out how to store the simplest data point using AWS services. After that,
we will add more features, convenient helpers, etc.

For this project, we will implement a REST API service for a uniform interface.
In respect to the serverless framework (and architecture):

Whenever a user call the using the API endpoint a POST request, the lambda
`create` function should store (validate either by the gateway or the lambda) the
data served through that request in DynamoDB. Similarly, when a user invokes
with a GET request, the `read` function will execute and send a response.

- Functions: 
    * create
    * read
    * scan (for browsing)
    * update (mark finished)
    * delete (extra feature)

- Event: An AWS API Gateway HTTP endpoint request (a GET/POST request)
- Resource: An AWS DyanomDB table

Database schema:
* DynamoDB needs a primary key. It could be a hash, or a string. 
Three options are available: 
    - use the partition key as primary key
    - use the partition and sort key as composite primary key
    - create a ticket_id. (we need to scan in that case for reading)
If the I choose to go with the latter, sort key = priority. 

* Other fields it should have: 
    - summary: string
    - created_at: timestamp/string (how to use
      [here](https://stackoverflow.com/questions/40561484/what-data-type-should-be-use-for-timestamp-in-dynamodb)
    - description: string
    - priority: string
    - completion_time: timestamp/string/float

I need to figure out a way to retrieve an item. Possible options:
1. Use the created_at timestamp (obvious, *can* be tedius)
2. Use the sort key to get a range of items (is it possible?)
3. Look at LSI

### To Do
- [x] Add function descriptions in `serverless.yml`
- [ ] Provide appropriate permissions for the functions
- [ ] Supply the right configs for the events (AWS API Gateway)
- [x] Set up the DynamoDB table(resources)
- [ ] Provide appropriate IAM access for functions. Come up with a convenient
way to call the create method
- [x] Validate data before putting into DynamoDB
- [ ] `create` function: check whether the item is duplicate before replacing
- [ ] `get` function: solve the KeyError issue


### Progres
- [x] Deployed the hello world app
- [x] Setting up the DynamoDB table (wip)
- [x] Deployed a test GET api method
- [x] Implemented a hardcoded create function
- [x] Implemented a scan function

### Prereq
- Node v4 or higher
- serverless framework

### Tools 
- AWS Lambda
- AWS API Gateway (with Lambda-Proxy integration, default on serverless)
- Serverless Framework

### Learning from this exercise
- Serverless architecture can be a great model for reducing operationals cost,
and depending on the organization, the server management could be completely
gone.
- DynamoDB's strength lie in its distributive nature. So it is crucial that even
distributions across the partitions are ensured by choosing a partition key
with high cardinality.
- The serverless framework (not the architecture) reduces a lot of pain points
that comes with deploying a non-trivial app in a serverless model. For AWS,
this framework produces a CloudFormation template and deploy resources in a
systematic way
- The serverless framework also provides AWS API Gateway, which makes dev's life
significantly easier. By taking care of things like that, serverless allow the
developer to focus on the features of their program.
- AWS Lambda is a great choice for orgs that uses functional programming as
their primary paradigm of developemnt. AWS Lambda is suppossed to be programmed in a
stateless manner.
- There is an odd error with CloudFormation that is if you change some
attributename in DynamoDB, you need to renamce the table name, and the rename
back, for the case when you just want to replace the name of the column. In
general, the paradigm will take more time to mature.
