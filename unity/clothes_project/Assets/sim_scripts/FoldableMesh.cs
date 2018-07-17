using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using AutoGeneration;



[System.Serializable]
public class FoldableMesh : MonoBehaviour {

    public GameObject curMesh;
    public MeshFilter curMeshName;
    public MeshRenderer curMeshRenderer;
    // public autotwoface double_sided;
    // public autocloth cloth_simulation;
    string m_path;

    // Use this for initialization

    private void Awake()
    {
        Debug.Log("awake");

        m_path = Application.dataPath;

        curMesh = new GameObject("Our Model");

        curMeshName = curMesh.AddComponent<MeshFilter>();
        curMesh.AddComponent<MeshRenderer>();
    }


    void Start()
    {

        Mesh mesh = curMesh.GetComponent<MeshFilter>().mesh;
        mesh = (Mesh)Resources.Load(m_path + "/Mesh/woman.fbx", typeof(Mesh));

    }


	// Update is called once per frame
	void Update () {
		
	}
}
