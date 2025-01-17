document.getElementById('generateBlogButton').addEventListener('click', async () => {

    const youtubeLink = document.getElementById('youtubeLink').value;
    const loadingIndicator = document.getElementById('loading');
    const blogContent = document.getElementById('blogContent');

    if(youtubeLink) {
        document.getElementById('loading-circle').style.display = 'block';
        loadingIndicator.classList.remove('hidden');
        blogContent.innerHTML(''); // Clear previous content

        const endpointUrl = '/generate-blog';

        try {
            const response = await fetch(endpointUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ link: youtubeLink })
            });

            const data = await response.json();

            blogContent.innerHTML = data.content;
            loadingIndicator.classList.add('hidden');

        }   catch (error) {
            console.error("Error occured:", error);
            alert("Something went wrong. try again later.");
            loadingIndicator.classList.add('hidden');
        }
        document.getElementById('loading-circle').style.display = 'none';
    }else {
        alert('Please enter a YouTube Link');
    }
});