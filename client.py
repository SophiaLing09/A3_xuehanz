import grpc
import reddit_pb2
import reddit_pb2_grpc

def run_tests():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reddit_pb2_grpc.RedditServiceStub(channel)
        test_create_post(stub)
        test_upvote_post(stub)
        test_downvote_post(stub)
        test_retrieve_post_content(stub)
        test_create_comment(stub)
        test_upvote_comment(stub)
        test_downvote_comment(stub)
        test_retrieve_top_comments(stub)
        test_expand_comment_branch(stub)

# This is the test to create post
def test_create_post(stub):
    new_post = reddit_pb2.Post( # Create an example
        id="1", 
        title="Post 001", 
        text="This is a test for the post 001.",
        author_id="Alice" 
    )
    response = stub.CreatePost(new_post)
    assert response.id == new_post.id, "Error: Response ID does not match request ID"
    assert response.title == new_post.title, "Error: Response title does not match request title"
    assert response.text == new_post.text, "Error: Response text does not match request text"
    assert response.author_id == new_post.author_id, "Error: Response author_id does not match request author_id"
    print("CreatePost test passed.")

# This is a test to upvote the post
def test_upvote_post(stub):
    # Create an example
    new_post = reddit_pb2.Post(id="2", title="Test Post 002", text="This is a test post 002.")
    stub.CreatePost(new_post)
    post_to_upvote = reddit_pb2.Post(id="2")
    response = stub.UpvotePost(post_to_upvote)
    assert response.score >= 1, "Post score did not increment as expected"
    print("UpvotePost test passed.")

# This is a test to downvote the post
def test_downvote_post(stub):
    # Create an example
    new_post = reddit_pb2.Post(id="3", title="Test Post 003", text="This is a test post 003")
    stub.CreatePost(new_post)
    post_to_downvote = reddit_pb2.Post(id="3")
    response = stub.DownvotePost(post_to_downvote)
    assert response.score <= 0, "Post score did not decrement as expected"
    print("DownvotePost test passed.")

# This is a test to retrieve the post
def test_retrieve_post_content(stub):
    # Create an example
    new_post = reddit_pb2.Post(
        id="4", 
        title="Test Post 004", 
        text="This is a test post 004",
        author_id="Daisy"  
    )
    stub.CreatePost(new_post)
    post_request = reddit_pb2.Post(id="4")
    response = stub.RetrievePostContent(post_request)
    assert response.id == new_post.id, "Error: Response ID does not match request ID"
    assert response.title == new_post.title, "Error: Response title does not match request title"
    assert response.text == new_post.text, "Error: Response text does not match request text"
    assert response.author_id == new_post.author_id, "Error: Response author_id does not match request author_id"
    print("RetrievePostContent test passed.")

# This is a test to create comment
def test_create_comment(stub):
    # Create an example for post
    new_post = reddit_pb2.Post(id="5", title="Test Post 005", text="This is a test post 005")
    stub.CreatePost(new_post)
    # Create an example for comment
    new_comment = reddit_pb2.Comment(id="10", text="This is a test comment for 005", parent_post_id="5")
    response = stub.CreateComment(new_comment)
    assert response.text == new_comment.text, "Error: Comment text does not match"
    assert response.id == new_comment.id, "Error: Comment ID does not match"
    assert response.parent_post_id == new_comment.parent_post_id, "Error: Parent post ID does not match"
    print("CreateComment test passed.")

# This is a test for upvote comment
def test_upvote_comment(stub):
    comment = reddit_pb2.Comment(id="10")
    response = stub.UpvoteComment(comment)
    assert response.score >= 1  # Assuming the score can be incremented
    print("UpvoteComment test passed.")

# This is a test for downvote comment
def test_downvote_comment(stub):
    comment = reddit_pb2.Comment(id="10")
    response = stub.DownvoteComment(comment)
    assert response.score <= 0  # Assuming the score can be decremented
    print("DownvoteComment test passed.")

# This is a test to retrieve the top comment
def test_retrieve_top_comments(stub):
    request = reddit_pb2.RetrieveTopCommentsRequest(post_id="1", n=5)
    response = stub.RetrieveTopComments(request)
    assert len(response.comments) <= 5, "More than 5 comments returned"
    print("RetrieveTopComments test passed.")

# This is a test for expand comment branch
def test_expand_comment_branch(stub):
    # Create some a comment and some child comment
    parent_comment = reddit_pb2.Comment(id="parent", text="Parent comment", score=5)
    stub.CreateComment(parent_comment)
    child_comment_1 = reddit_pb2.Comment(id="child1", text="Child comment 1", parent_comment_id="parent", score=3)
    stub.CreateComment(child_comment_1)
    child_comment_2 = reddit_pb2.Comment(id="child2", text="Child comment 2", parent_comment_id="parent", score=10)
    stub.CreateComment(child_comment_2)
    request = reddit_pb2.CommentBranchRequest(comment_id="parent", n=2)
    response = stub.ExpandCommentBranch(request)
    assert len(response.comments) <= 2, "Returned more comments than requested"
    if len(response.comments) > 0:
        assert response.comments[0].id == "child2", "First comment should be the most upvoted one"
    print("ExpandCommentBranch test passed.")

if __name__ == '__main__':
    run_tests()