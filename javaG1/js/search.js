function fetchData() {
    var name = document.getElementById('queryInput').value;
    var category = document.getElementById('categorySelect').value;
    var apiUrl = 'http://tejdemo.ddns.net/api/g2/' + category + '/' + name;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => displayResult(data))
        .catch(error => console.error('Error fetching data:', error));
}

async function displayResult(data) {
    var container = document.getElementById('container');
    container.innerHTML = '';

    var customOrder = ['cookbookName', 'cookbookDesc', 'cookTime', 'serving', 'chefName'];

    for (const item of data) {
        var jsonBlock = createJsonBlock(item, customOrder);
        var likeInfoElement = createLikeInfoElement(item);

        // 將 rightBlock 添加到 .right-block 中
        var rightBlock = document.createElement('div');
        rightBlock.classList.add('right-block');

        // 使用 await 等待 fetchAndDisplayRightBlock 完成，並將 rightBlock 添加內容到 right-block 中
        await fetchAndDisplayRightBlock(item.cookbookID, rightBlock)
            .catch(error => console.error('Error:', error));

        // 將 jsonBlock、likeInfoElement、rightBlock 添加到 container 中
        container.appendChild(jsonBlock);
        container.appendChild(likeInfoElement);
        container.appendChild(rightBlock);
    }
}



function createJsonBlock(item, customOrder) {
    var jsonBlock = document.createElement('div');
    jsonBlock.classList.add('json-container', 'json-item');

    customOrder.forEach(key => {
        if (item.hasOwnProperty(key)) {
            var blockSeparator = document.createElement('hr');
            blockSeparator.classList.add('block-separator');

            var titleElement = document.createElement('div');
            titleElement.classList.add('title');
            titleElement.innerText = getCustomTitle(key);

            var contentElement = document.createElement('div');
            contentElement.classList.add('content');
            contentElement.innerText = item[key] || item[key] === 0 ? item[key] : '無';

            jsonBlock.appendChild(blockSeparator);
            jsonBlock.appendChild(titleElement);
            jsonBlock.appendChild(contentElement);
        }
    });

    return jsonBlock;
}

function createLikeInfoElement(item) {
    var likeInfoElement = document.createElement('div');
    likeInfoElement.classList.add('like-info');

    ['loveTag', 'tastyTag', 'goodTag'].forEach(tag => {
        var tagElement = document.createElement('div');
        tagElement.classList.add('tag');

        var titleElement = document.createElement('div');
        titleElement.classList.add('title');
        titleElement.innerText = getCustomLikeTitle(tag);

        var contentElement = document.createElement('div');
        contentElement.classList.add('content');
        contentElement.innerText = item[tag] || item[tag] === 0 ? item[tag] : '無';

        tagElement.appendChild(titleElement);
        tagElement.appendChild(contentElement);

        likeInfoElement.appendChild(tagElement);
    });

    return likeInfoElement;
}

// function createContainer(jsonBlock, likeInfoElement) {
//     var container = document.createElement('div');
//     container.classList.add('json-result-container');
//     container.appendChild(jsonBlock);
//     container.appendChild(likeInfoElement);

//     return container;
// }

function getCustomTitle(key) {
    switch (key) {
        case 'cookbookDesc':
            return '食譜簡介';
        case 'loveTag':
            return '愛心次數';
        case 'tastyTag':
            return '好吃次數';
        case 'cookbookName':
            return '食譜名稱';
        case 'cookTime':
            return '烹飪時間';
        case 'chefName':
            return '廚師名稱';
        case 'goodTag':
            return '按讚次數';
        case 'serving':
            return '食譜分量';
        default:
            return '';
    }
}

function getCustomLikeTitle(tag) {
    switch (tag) {
        case 'loveTag':
            return '愛心次數';
        case 'tastyTag':
            return '好吃次數';
        case 'goodTag':
            return '按讚次數';
        default:
            return '';
    }
}

function fetchAndDisplayRightBlock(cookbookID, rightBlock) {
    var rightBlockApiUrl = 'http://tejdemo.ddns.net/api/g2/cookbook/steps/' + cookbookID;

    return fetch(rightBlockApiUrl)
        .then(response => response.json())
        .then(rightBlockData => {
            rightBlockData.forEach(item => {
                var customOrder = ['stepDesc'];
                customOrder.forEach(key => {
                    if (item.hasOwnProperty(key)) {
                        var blockSeparator = document.createElement('hr');
                        blockSeparator.classList.add('block-separator');

                        var titleElement = document.createElement('div');
                        titleElement.classList.add('title');
                        titleElement.innerText = '食譜步驟';

                        var contentElement = document.createElement('div');
                        contentElement.classList.add('content');
                        contentElement.innerText = item[key] || item[key] === 0 ? item[key] : '無';

                        rightBlock.appendChild(blockSeparator);
                        rightBlock.appendChild(titleElement);
                        rightBlock.appendChild(contentElement);
                    }
                });
            });
        })
        .catch(error => console.error('Error fetching right block data:', error));
}
