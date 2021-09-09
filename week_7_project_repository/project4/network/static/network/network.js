//once content loaded attache event listeners to buttons
document.addEventListener('DOMContentLoaded', function() {
   console.log("DOM loaded")
   //hide compose view
   document.querySelector('#createNewPost-view').style.display = 'none';
    //add event listeners to buttons
    document.querySelector('#createNewPost').addEventListener('click', () => compose('compose'));
    document.querySelector('#cancelNewPost').addEventListener('click', ()=>{
        document.querySelector('#createNewPost-view').style.display = 'none';
    })
    document.querySelector('#followbtn').addEventListener('click', ()=>{
        followBtn = document.querySelector('#followbtn')
        if(followBtn.value == "Follow"){
            fetch('/follow',{
                method: 'POST', 
                body: JSON.stringify({
                    userToFollow: document.querySelector('#profile_user').innerHTML,
                    followRequest: "follow",
                })
            })
            .then(response => response.json())
                .then(result => {
                // Print result
                console.log(result);
            });

            followBtn.innerHTML = "Unfollow";
            followBtn.value = "Unfollow";
        }
        else{
            fetch('/follow',{
                method: 'POST', 
                body: JSON.stringify({
                    userToFollow: document.querySelector('#profile_user').innerHTML,
                    followRequest: "unfollow",
                })
            })
            .then(response => response.json())
                .then(result => {
                // Print result
                console.log(result);
            });
            followBtn.innerHTML = "Follow";
            followBtn.value = "Follow";
        }

    })
});

function compose(type){
    console.log("loading compose form");
    document.querySelector('#createNewPost-view').style.display = 'block';
}