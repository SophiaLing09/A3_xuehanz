# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creddit.proto\x12\x06reddit\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xde\x01\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x17\n\x0fvideo_image_url\x18\x04 \x01(\t\x12\r\n\x05score\x18\x05 \x01(\x05\x12&\n\x05state\x18\x06 \x01(\x0e\x32\x17.reddit.Post.State_post\x12\x18\n\x10publication_date\x18\x07 \x01(\t\x12\x11\n\tauthor_id\x18\x08 \x01(\t\"0\n\nState_post\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\n\n\x06HIDDEN\x10\x02\"\xcf\x01\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\tauthor_id\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x05\x12,\n\x05state\x18\x05 \x01(\x0e\x32\x1d.reddit.Comment.State_comment\x12\x16\n\x0eparent_post_id\x18\x06 \x01(\t\x12\x19\n\x11parent_comment_id\x18\x07 \x01(\t\"\'\n\rState_comment\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06HIDDEN\x10\x01\"8\n\x1aRetrieveTopCommentsRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\x05\"5\n\x14\x43ommentBranchRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\x05\"O\n\x15\x43ommentBranchResponse\x12!\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x0f.reddit.Comment\x12\x13\n\x0bhas_replies\x18\x02 \x01(\x08\x32\x8b\x04\n\rRedditService\x12(\n\nCreatePost\x12\x0c.reddit.Post\x1a\x0c.reddit.Post\x12(\n\nUpvotePost\x12\x0c.reddit.Post\x1a\x0c.reddit.Post\x12*\n\x0c\x44ownvotePost\x12\x0c.reddit.Post\x1a\x0c.reddit.Post\x12\x31\n\x13RetrievePostContent\x12\x0c.reddit.Post\x1a\x0c.reddit.Post\x12\x31\n\rCreateComment\x12\x0f.reddit.Comment\x1a\x0f.reddit.Comment\x12\x31\n\rUpvoteComment\x12\x0f.reddit.Comment\x1a\x0f.reddit.Comment\x12\x33\n\x0f\x44ownvoteComment\x12\x0f.reddit.Comment\x1a\x0f.reddit.Comment\x12X\n\x13RetrieveTopComments\x12\".reddit.RetrieveTopCommentsRequest\x1a\x1d.reddit.CommentBranchResponse\x12R\n\x13\x45xpandCommentBranch\x12\x1c.reddit.CommentBranchRequest\x1a\x1d.reddit.CommentBranchResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=24
  _globals['_USER']._serialized_end=47
  _globals['_POST']._serialized_start=50
  _globals['_POST']._serialized_end=272
  _globals['_POST_STATE_POST']._serialized_start=224
  _globals['_POST_STATE_POST']._serialized_end=272
  _globals['_COMMENT']._serialized_start=275
  _globals['_COMMENT']._serialized_end=482
  _globals['_COMMENT_STATE_COMMENT']._serialized_start=443
  _globals['_COMMENT_STATE_COMMENT']._serialized_end=482
  _globals['_RETRIEVETOPCOMMENTSREQUEST']._serialized_start=484
  _globals['_RETRIEVETOPCOMMENTSREQUEST']._serialized_end=540
  _globals['_COMMENTBRANCHREQUEST']._serialized_start=542
  _globals['_COMMENTBRANCHREQUEST']._serialized_end=595
  _globals['_COMMENTBRANCHRESPONSE']._serialized_start=597
  _globals['_COMMENTBRANCHRESPONSE']._serialized_end=676
  _globals['_REDDITSERVICE']._serialized_start=679
  _globals['_REDDITSERVICE']._serialized_end=1202
# @@protoc_insertion_point(module_scope)
