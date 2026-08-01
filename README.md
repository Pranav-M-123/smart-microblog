# Smart Microblog

A Python-based microblogging platform that includes real-time sentiment analysis and a custom frontend interface.

## Features
* **Sentiment Analysis:** Uses TextBlob to analyze the mood of user posts and color-codes the feed based on the result (Positive, Negative, Neutral).
* **Custom UI:** Includes a glassmorphism design system, scroll-reveal animations using IntersectionObserver, and card-based layouts.
* **Authentication:** User registration and login handled with Werkzeug password hashing and Flask-Login session management.
* **Social Features:** Users can follow and unfollow others, track follower counts, and see who follows them back.
* **Post Management:** Users can create, edit, like, and delete posts. The timeline includes pagination for managing large volumes of data.
* **Asynchronous Updates:** Uses background AJAX polling to update the timeline when new posts are created without refreshing the page.

## Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite, Flask-SQLAlchemy
* **NLP:** TextBlob
* **Frontend:** HTML, CSS, Vanilla JS

## Setup Instructions

**1. Clone the repository:**
```bash
git clone [https://github.com/Pranav-M-123/smart-microblog.git](https://github.com/Pranav-M-123/smart-microblog.git)
cd smart-microblog
