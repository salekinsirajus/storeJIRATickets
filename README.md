# Ticket Interface
Stores and retrieves summary of JIRA tickets; solved as a code assignment

## Instructions
The customer wishes to build a system storing summary information about their
internal JIRA tickets.  In short, the system will:

- [ ] Receive POST notifications from JIRA
- [ ] Store relevant fields from the notifications
- [ ] If applicable, calculate the time between ticket created and ticket closed
- [ ] Provide an ability to retrieve the records via a GET request.
 

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

### To Do
- [ ] Where and how to store the JSON
- [ ] How to read from the database (figure out a standard way to do this)
