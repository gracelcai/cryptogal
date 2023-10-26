# CryptoGal
## Inspiration
We were interested in educating young women about finance as a form of empowerment. We decided to take the crypto route as it is always a topic of discussion in the finance world. We wanted to analyze crypto with data science and APIs. We drew inspiration from other finance projects such as FinWhiz.

## What it does
We help women succeed in crypto by promoting financial literacy, providing up-to-date information, and finding positive role models. CryptoGal contains four main features.

CryptoGal is able to compare the fundamentals of different cryptocurrencies. Through dropdown menus, the user is able to select up to 10 different cryptocurrencies and choose start and end dates to analyze a specific time frame and access real-time data. The information is stored in a table that analyzes each cryptocurrency and calculates their opening value, closing value, highs, lows, adjusted closing price, and volume – allowing users to understand the various attributes of these cryptocurrencies.
The Crypto Tracker shows the latest information from Yahoo Finance about the price changes in the cryptocurrency market. It creates two line charts to analyze the adjusted closing price and cumulative returns over time for each coin. Understanding the crypto market teaches users the causes for how the value of each coin can change.
The Women in Crypto feature introduces users to inspiring women making strides in the blockchain and crypto industries. Women working in these fields are able to connect with users through networking in various social media platforms, starting companies, releasing articles about their experiences, and passing inclusive public policy. Here, CryptoGal aims to build a tight-knit community with supportive mentors, encouraging young women to learn more about crypto.
The Reports feature shares informative and in-depth articles about learning to trade cryptocurrencies. All compiled in one place, these articles are an effective medium to show the basics of crypto and allow users to gain a deeper understanding of the field before they try it out themselves.

## How we built it
On the backend of the Crypto Tracker, we used Python’s Pandas library to analyze data from various cryptocurrencies. To retrieve real-time cryptocurrency data, we used the Yahoo Finance API. We displayed the data visualization with Streamlit.

UI/UX: Figma

Frontend: HTML, CSS, Javascript,

Backend: Python, Pandas, Streamlit

## Challenges we ran into
In the beginning, we had planned to use CockroachDB to store cryptocurrency data. However, it was difficult to set up and there were not many resources out there to guide us as we had never used it before. Then, after looking online for tutorials on retrieving and displaying cryptocurrency data, we found that we could directly get data from the Yahoo Finance API in real-time and display it with Streamlit. This was much simpler to set up and deploy quickly.

To work as efficiently as possible, we split up the crypto tracker and the other pages on the frontend. But after we finished creating each part, we were unable to connect them as the crypto tracker uses Streamlit, which is in Python, but the other pages use HTML and CSS. We found that Streamlit had HTML components, but the CSS did not transfer when we tried using an HTML component.

## Accomplishments that we're proud of
We are proud of having learned how to use Streamlit, as well as integrating the Yahoo Finance API in such a short amount of time. A lot of us also learned front end for the first time in this hackathon, so it was a great experience to learn HTML, CSS and Javascript.

## What we learned
We learned new technologies for data science including Streamlit and the Yahoo Finance API. Not only that, but we also learned a lot about cryptocurrencies as well as women in finance from the research we did for this project.

## What's next for CryptoGal
We plan on adding more functions to our Crypto Tracker such as a predictor to help users decide which cryptocurrencies to invest in. In addition, we would like to add more resources and information about different cryptocurrencies and women in finance to encourage young women to invest in crypto.

## Try It
Frontend https://l3qiz1.csb.app/

Backend (Real-Time Analytics) https://share.streamlit.io/gracelcai/superposition-vi/main/crypto_tracker.py

## Sources
Why Women Are Better Investors – Forbes Advisor
Wef 2022: Why Web3 Needs More Women In Spearheading Positions
Environmentally Friendly Cryptocurrency
6 Women Who Are Changing the Face — and Future — of Crypto
https://medium.com/the-capital/women-in-blockchain-where-are-they-e4e2341b19ce
https://simpleswap.io/blog/women-in-crypto
https://www.buybitcoinworldwide.com/cryptocurrency-statistics/
