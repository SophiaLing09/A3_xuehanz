import grpc
from concurrent import futures
import reddit_pb2
import reddit_pb2_grpc

posts = {}
comments = {}

class RedditService(reddit_pb2_grpc.RedditServiceServicer):

    # This is the function to create post
    def CreatePost(self, request, context):
        new_post = request
        # Check if the id exists
        if new_post.id in posts:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details('Post already exists. ID: ' + new_post.id)
            return reddit_pb2.Post()
        # Store new post in the list
        posts[new_post.id] = new_post
        return new_post

    # This is the function to upvote a post 
    def UpvotePost(self, request, context):
        # Check if the id exists
        if request.id not in posts:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Post not found. ID: ' + request.id)
            return reddit_pb2.Post()
        # Upvote the post
        post = posts[request.id]
        post.score += 1 # The number should increase
        return post

    # This is the function to downvote 
    def DownvotePost(self, request, context):
        # Check if the id exists
        if request.id not in posts:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Post not found. ID: ' + request.id)
            return reddit_pb2.Post()
        # Downvote the post
        post = posts[request.id]
        post.score -= 1
        return post

    # This is the function to retrieve the post
    def RetrievePostContent(self, request, context):
        # Retrieve the post
        return posts.get(request.id, reddit_pb2.Post())

    # This is the function to create a comment
    def CreateComment(self, request, context):
        # Create a comment
        comments[request.id] = request
        return request

    # This is the function to upvote the comment
    def UpvoteComment(self, request, context):
        # Upvote a comment
        if request.id in comments:
            comments[request.id].score += 1
        return comments.get(request.id, reddit_pb2.Comment())

    # This is the function to downvote the comment
    def DownvoteComment(self, request, context):
        # Downvota a comment
        if request.id in comments:
            comments[request.id].score -= 1
        return comments.get(request.id, reddit_pb2.Comment())

    # This is the function to retrieve the top comment
    def RetrieveTopComments(self, request, context):
        top_comments = sorted(
            [c for c in comments.values() if c.parent_post_id == request.post_id],
            key=lambda c: c.score, reverse=True
        )[:request.n]
        has_replies = any(
            any(child_comment.parent_comment_id == comment.id for child_comment in comments.values())
            for comment in top_comments
        )
        return reddit_pb2.CommentBranchResponse(comments=top_comments, has_replies=has_replies)

    # This is the function to expand comment branch
    def ExpandCommentBranch(self, request, context):
        top_child_comments = sorted(
            [c for c in comments.values() if c.parent_comment_id == request.comment_id],
            key=lambda c: c.score, reverse=True
        )[:request.n]
        has_replies = any(
            any(child_comment.parent_comment_id == comment.id for child_comment in comments.values())
            for comment in top_child_comments
        )
        return reddit_pb2.CommentBranchResponse(comments=top_child_comments, has_replies=has_replies)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()