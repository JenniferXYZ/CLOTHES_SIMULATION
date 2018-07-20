using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using AutoGeneration;
using UnityEditor;
using UnityEngineInternal;


[System.Serializable]
//[ExecuteInEditMode]
public class FoldableMesh : MonoBehaviour
{

    public GameObject curMesh;
    public MeshFilter curMeshName;
    public MeshRenderer curMeshRenderer;
    //public autotwoface double_sided;
    //public autocloth cloth_simulation;
    string m_path;
    string FBX_name;
    // private Color materialColors;

    // Use this for initialization

    private void Awake()
    {
        //Debug.Log("awake");

        m_path = Application.dataPath;



        curMesh = new GameObject("Our Model");
        curMeshName = curMesh.AddComponent<MeshFilter>();
        curMeshRenderer = curMesh.AddComponent<MeshRenderer>();

        /* Name the file to be loaded */
        FBX_name = "tri_15_tex";

        Mesh mesh;
        mesh = (Mesh)Resources.Load(FBX_name, typeof(Mesh));
        curMeshName.sharedMesh = (Mesh)Resources.Load(FBX_name, typeof(Mesh));
        curMeshRenderer.material = (Material)Resources.Load(FBX_name, typeof(Material));

        curMesh.transform.eulerAngles = new Vector3(transform.eulerAngles.x, 90, transform.eulerAngles.z);
        curMesh.transform.position = new Vector3(2, 1, 1);


        curMesh.AddComponent<autotwoface>();
        curMesh.AddComponent<autocloth>();

        //Debug.Log(Time.deltaTime);


    }


    void Start()
    {

    }




    // Update is called once per frame
    void Update()
    {

    }
}
