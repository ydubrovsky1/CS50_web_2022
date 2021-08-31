//once content loaded attache event listeners to buttons
document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
 

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  //add event listener for form submission
   // Listen for submission of form
   document.querySelector('form').onsubmit = () => {
      //on submission, fetch /emails with POST method, adding new email
      fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
            recipients: document.querySelector('#compose-recipients').value,
            subject: document.querySelector('#compose-subject').value,
            body: document.querySelector('#compose-body').value
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
          console.log(result);
      });
   }
}

function load_mailbox(mailbox) {
  console.log("loading mailbox")
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  //send a GET request to URL
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);
      console.log("logged once")
      // ... do something else with emails ...
      emails.forEach(add_post);

      function add_post(email) {
        // Create new post
        const post = document.createElement('div');
        if (email.read){
          post.style.backgroundColor = '#1A90CE';
        }
        else{
          post.style.backgroundColor = '#b7f0fc';
        }
        //use data in email object to update post properties
        post.className = 'post';
        post.sender = email.sender;
        post.subject = email.subject;
        post.timestamp = email.timestamp;
        post.body = email.body;
        post.recipients = email.recipients;
        post.id = email.id;
        post.read = email.read;
        post.archived = email.archived;
        post.innerHTML = `sender: <b>${post.sender}</b> | subject: <b>${post.subject}</b> | receieved: ${post.timestamp}`;
        //add event listener to the post (for user click)
        post.addEventListener('click', function() {
          console.log('This email has been clicked!')
            //set email's read status to true
            fetch(`/emails/${post.id}`, {
              method: 'PUT',
              body: JSON.stringify({
                read: true
              })
            })

          //call function to view email
          view_email(post);
        });
        console.log("finished loading mailbox")
        // Add post to DOM
        document.querySelector('#emails-view').append(post);
    };
    
  });
}

function view_email(post){
  // Show email view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#subject').innerHTML = `subject: ${post.subject}`;
  document.querySelector('#sender').innerHTML = `sender: ${post.sender}`;
  document.querySelector('#timestamp').innerHTML = `received: ${post.timestamp}`;
  document.querySelector('#email_body').innerHTML = post.body;
  document.querySelector('#recipients').innerHTML = `recipients: ${post.recipients}`;

    //allow user to archive or unarchive depending
    var isArchived = false;
    document.querySelector('#archive_button').innerHTML = "Archive";
    if (post.archived){
      document.querySelector('#archive_button').innerHTML = "UnArchive";
      isArchived = true;
    }

  //allow use to archive 
  const archive_button = document.querySelector('#archive_button');
  archive_button.addEventListener('click', archiveFunction(post, isArchived));
  function archiveFunction(post, isArchived){
    console.log(`post:${post} isArchived: ${isArchived}`)
  }  


  //allow user to reply
  document.querySelector('#reply').addEventListener('click', function(){
    console.log('This reply element has been clicked!')
    compose_reply_email(post);
  });

}


//compose email function with prefilled values
function compose_reply_email(post) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Prefill composition fields--value and Html
  document.querySelector('#compose-recipients').value = post.sender;
  document.querySelector('#compose-recipients').innerHTML = post.sender;
  document.querySelector('#compose-subject').value = `re: ${post.subject}`;
  document.querySelector('#compose-subject').innerHTML = `re: ${post.subject}`;
  document.querySelector('#compose-body').value = `\non ${post.timestamp} ${post.sender} wrote: ${post.body}`;
  document.querySelector('#compose-body').innerHTML = `\non ${post.timestamp} ${post.sender} wrote: ${post.body}`;

  //add event listener for form submission
   // Listen for submission of form
   document.querySelector('form').onsubmit = () => {
      //on submission, fetch /emails with POST method, adding new email
      fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
            recipients: document.querySelector('#compose-recipients').value,
            subject: document.querySelector('#compose-subject').value,
            body: document.querySelector('#compose-body').value
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
          console.log(result);
      });
   }
}

