// Handle file upload preview
document.addEventListener('DOMContentLoaded', function() {
    const uploadInput = document.getElementById('signImage');
    const previewDiv = document.getElementById('preview');
    
    if (uploadInput && previewDiv) {
        uploadInput.addEventListener('change', function(e) {
            if (e.target.files.length > 0) {
                const file = e.target.files[0];
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    previewDiv.innerHTML = `<img src="${e.target.result}" class="img-thumbnail mt-2" style="max-height: 200px;">`;
                }
                
                reader.readAsDataURL(file);
            }
        });
    }
});
