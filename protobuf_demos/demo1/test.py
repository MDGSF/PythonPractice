#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from google.protobuf.json_format import MessageToJson
import object_pb2


def main():
    obj_list = object_pb2.ObjectList()
    obj_list.source_info.file_path = "/test/"
    obj_list.source_info.frame_num = 123

    obj1 = object_pb2.Object()
    obj1.id = 1
    obj_list.list.append(obj1)

    print(obj_list)

    json_obj_list = MessageToJson(obj_list)
    print(json_obj_list)

    b = obj_list.SerializeToString()
    print(b)


if __name__ == "__main__":
    main()
